import asyncio
import json

import execjs
import websockets

async def hello():
    uri = "wss://www.python-spider.com/api/challenge61"  # 替换为你的WebSocket服务器地址
    async with websockets.connect(uri) as websocket:
        sum = 0
        for i in range(1,101):
            with open("demo.js", "r", encoding="utf-8") as file:
                jscode = file.read()
                ctx = execjs.compile(jscode)
                ctx = ctx.call("decode_send", i)
            await websocket.send(f"{ctx}")
            response = await websocket.recv()
            print(f"Received: {response}")
            Data = json.loads(response)
            for data in Data['data']:
                sum+=int(data['value'])
        print(sum)

asyncio.get_event_loop().run_until_complete(hello())