import asyncio
import json
import logging
import random
import time

import requests
from async_retrying import retry

import pandas as pd
from playwright.async_api import async_playwright
from functools import reduce


def merge_tennis_data(list1, list2, list3):
    """
    合并三个列表中的网球比赛数据

    参数:
        list1, list2, list3: 包含比赛字典的三个列表

    返回:
        合并后的DataFrame
    """
    # 定义关键列用于合并
    key_columns = ['Data', 'Tournament', 'Surface', 'Rd', 'Rk', 'vRk',
                   'JessicaPegula', 'Score', 'Time']

    # 将三个列表转换为DataFrame
    df1 = pd.DataFrame(list1)
    df2 = pd.DataFrame(list2)
    df3 = pd.DataFrame(list3)

    # 数据清洗函数
    def clean_data(df):
        # 转换日期和数值
        # df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
        numeric_cols = ['Rk', 'vRk', 'TP', 'Aces', 'DFs', 'SP', '1SP', '2SP', 'vA']
        for col in numeric_cols:
            if col in df:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # 清理字符串中的特殊字符
        str_cols = df.select_dtypes(include='object').columns
        for col in str_cols:
            df[col] = df[col].str.replace('\xa0', ' ').str.strip()

        return df

    # 清洗所有DataFrame
    df1 = clean_data(df1)
    df2 = clean_data(df2)
    df3 = clean_data(df3)

    # 合并策略 - 保留非空值
    def merge_two_dfs(left, right):
        return pd.merge(
            left, right,
            on=key_columns,
            how='outer',
            suffixes=('', '_drop')
        ).filter(regex='^(?!.*_drop)')

    # 逐步合并三个DataFrame
    merged_df = reduce(merge_two_dfs, [df1, df2, df3])

    # 处理合并后的重复列 (当不同列表有相同列但不同值时)
    for col in merged_df.columns:
        if col not in key_columns:
            # 找出所有可能的列变体 (如A%, A%_x, A%_y等)
            similar_cols = [c for c in merged_df.columns if c.startswith(col)]
            if len(similar_cols) > 1:
                # 合并这些列，优先使用非空值
                merged_df[col] = merged_df[similar_cols].bfill(axis=1).iloc[:, 0]
                # 删除临时列
                merged_df.drop(columns=[c for c in similar_cols if c != col], inplace=True)

    # 对百分比列进行统一处理
    # percent_cols = [col for col in merged_df.columns if col.endswith('%')]
    # for col in percent_cols:
    #     merged_df[col] = merged_df[col].str.rstrip('%').astype(float) / 100

    # 按日期排序
    merged_df.sort_values(by=['Data', 'Tournament', 'Rd'], inplace=True)

    return merged_df.reset_index(drop=True)




class TennisCrawler:
    def __init__(self, headless=True):
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
        }

    async def InitBrowser(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True,
            args=[
                '--disable-gpu',
                '--single-process',  # 单进程模式
                '--no-zygote',
                '--no-sandbox'
            ],
            # 禁用不必要功能
            chromium_sandbox=False,
            downloads_path=None,
            ignore_default_args=[
                '--disable-extensions',
                '--enable-automation'
            ]
    )
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()
    async def GetOnePlayersInfoFromServe(self,name):

        await self.page.goto(f"https://www.tennisabstract.com/cgi-bin/player-classic.cgi?p={name}&f=ACareerqq", wait_until="domcontentloaded")
        # 使用evaluate一次性获取所有数据
        data = await self.page.evaluate('''() => {
            const rows = document.querySelectorAll("table#matches tbody tr");
            return Array.from(rows).map(row => {
                const cells = row.querySelectorAll("td");
                return {
                    'Data': cells[0]?.textContent.trim(),
                    'Tournament': cells[1]?.textContent.trim(),
                    'Surface': cells[2]?.textContent.trim(),
                    'Rd': cells[3]?.textContent.trim(),
                    'Rk': cells[4]?.textContent.trim(),
                    'vRk': cells[5]?.textContent.trim(),
                    'JessicaPegula': cells[6]?.textContent.trim(),
                    'Score': cells[7]?.textContent.trim(),
                    'More': cells[8]?.textContent.trim(),
                    'DR': cells[9]?.textContent.trim(),
                    'A%': cells[10]?.textContent.trim(),
                    'DF%': cells[11]?.textContent.trim(),
                    '1stln': cells[12]?.textContent.trim(),
                    '1st%': cells[13]?.textContent.trim(),
                    '2nd%': cells[14]?.textContent.trim(),
                    'BPSaved': cells[15]?.textContent.trim(),
                    'Time': cells[16]?.textContent.trim()
                };
            });
        }''')
        return data
    async def GetOnePlayersInfoFromReturn(self,name):
        await self.page.goto(f"https://www.tennisabstract.com/cgi-bin/player-classic.cgi?p={name}&f=ACareerqqr1",wait_until="domcontentloaded")
        data = await self.page.evaluate('''() => {
                    const rows = document.querySelectorAll("table#matches tbody tr");
                    return Array.from(rows).map(row => {
                        const cells = row.querySelectorAll("td");
                        return {
                            'Data': cells[0]?.textContent.trim(),
                            'Tournament': cells[1]?.textContent.trim(),
                            'Surface': cells[2]?.textContent.trim(),
                            'Rd': cells[3]?.textContent.trim(),
                            'Rk': cells[4]?.textContent.trim(),
                            'vRk': cells[5]?.textContent.trim(),
                            'JessicaPegula': cells[6]?.textContent.trim(),
                            'Score': cells[7]?.textContent.trim(),
                            'More': cells[8]?.textContent.trim(),
                            'DR': cells[9]?.textContent.trim(),
                            'TPW': cells[10]?.textContent.trim(),
                            'PRW': cells[11]?.textContent.trim(),
                            'vA%': cells[12]?.textContent.trim(),
                            'v1st%': cells[13]?.textContent.trim(),
                            'v2nd%': cells[14]?.textContent.trim(),
                            'BPCnv': cells[15]?.textContent.trim(),
                            'Time': cells[16]?.textContent.trim()
                        };
                    });
                }''')



        return data
    async def GetOnePlayersInfoFromRaw(self,name):
        await self.page.goto(f"https://www.tennisabstract.com/cgi-bin/player-classic.cgi?p={name}&f=ACareerqqw1",wait_until="domcontentloaded")
        data = await self.page.evaluate('''() => {
                            const rows = document.querySelectorAll("table#matches tbody tr");
                            return Array.from(rows).map(row => {
                                const cells = row.querySelectorAll("td");
                                return {
                                    'Data': cells[0]?.textContent.trim(),
                                    'Tournament': cells[1]?.textContent.trim(),
                                    'Surface': cells[2]?.textContent.trim(),
                                    'Rd': cells[3]?.textContent.trim(),
                                    'Rk': cells[4]?.textContent.trim(),
                                    'vRk': cells[5]?.textContent.trim(),
                                    'JessicaPegula': cells[6]?.textContent.trim(),
                                    'Score': cells[7]?.textContent.trim(),
                                    'More': cells[8]?.textContent.trim(),
                                    'TP': cells[9]?.textContent.trim(),
                                    'Aces': cells[10]?.textContent.trim(),
                                    'DFs': cells[11]?.textContent.trim(),
                                    'SP': cells[12]?.textContent.trim(),
                                    '1SP': cells[13]?.textContent.trim(),
                                    '2SP': cells[14]?.textContent.trim(),
                                    'vA': cells[15]?.textContent.trim(),
                                    'Time': cells[16]?.textContent.trim()
                                };
                            });
                        }''')
        return data
    async def GetManPlayersName(self):
        with open("Man_cleaned_names.json", 'r', encoding='utf')as f:
            names_from_json = json.load(f)
            return names_from_json

    def dynamic_sleep(self,base_delay=1):
        """基础延迟 + 随机抖动"""
        delay = base_delay + random.uniform(0.2,1)
        time.sleep(delay)
    async def main(self,name):
        start_time = time.time()
        await self.InitBrowser()
        self.dynamic_sleep()
        list1=await self.GetOnePlayersInfoFromServe(name)
        self.dynamic_sleep()
        list2=await self.GetOnePlayersInfoFromReturn(name)
        self.dynamic_sleep()
        list3=await self.GetOnePlayersInfoFromRaw(name)
        await self.browser.close()
        await self.playwright.stop()
        print(f"{name}数据获取成功")
        result_df = merge_tennis_data(list1, list2, list3)
        # 显示结果
        pd.set_option('display.max_columns', None)
        # print("合并后的比赛数据:")
        # print(result_df)
        result_df.to_csv(f'./Data./{name}_merged_tennis_data.csv', index=False)
        end_time = time.time()
        pass_time = end_time - start_time
        print(f"数据已保存到 {name}_tennis_data.csv总计耗时{int(pass_time)}秒")

    async def GetAllMansPlayerInfo(self):
        AllNames = await self.GetManPlayersName()
        i = 1
        for name in AllNames:
            print(f"第{str(i)}个player正在获取")
            i+=1
            await self.main(name)



if __name__ == "__main__":
    asyncio.run(TennisCrawler().GetAllMansPlayerInfo())