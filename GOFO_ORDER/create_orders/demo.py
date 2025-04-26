import base64

import requests

url = "https://uat-dbu-api.eminxing.com/open-api/v2/order/create"


user = "AISOON"
password ="AISOON@0424"
authorization = f"{user}:{password}"
authorization_encode=base64.b64encode(authorization.encode()).decode()
header = {
    "Authorization" : f"Basic {authorization_encode}"
}

data = {
    "productType":"ECO",#非必填,服务类型，可以不传，默认为ECO，请传如下固定值 ECO：特惠 EXP：标快
    "shippingType":"HDN",#非必填,配送类型：HDN（送货上门），ZT（自提），默认为HDN(送货上门)
    "declaredValue":13,#包裹预报货值，单位：美金 范围0.0001-100.00 例如：13
    "orderShipper":{
        "shipperName":"louis",#发件人-姓名，长度为1-50
        "shipperPhone":"13678987875",#发件人-姓名，长度为1-50
        "shipperCountry":"China",#发件人-国家 根据实际情况，传China
        "shipperState":"Heilongjiang",#发件人-省/州 China - 省的名称的汉语拼音  州的名称 长度1-35例如：Heilongjiang
        "shipperCity":"Wulanchabu",#发件人-市 China - 市的名称的汉语拼音 Mexio - 市的名称长度1-50例如：Wulanchabu
        "shipperStreet":"309 Dongfeng Middle Rd",#发件人-详细地址 长度1-100
        "shipperCode":"224000",#发件人-详细地址 长度1-100

    },#寄件信息
    "orderConsignee":{
        "consigneeName":"louis",#收件人-姓名，长度为1-100
        "consigneePhone":"13678987875",#收件人手机号，长度为10-14
        "consigneeCountry":"US",#收件国家（具体可参考如下：收件国家简码对照表）
        "consigneeState":"XXXXXX",#收件人-州长度1-35
        "consigneeCity":"XXXXXX",#收件人-市长度1-50
        "consigneeArea":"XXXXXX",#非必填 收件人-区长度1-50
        "address1":"XXXXXX",#收件地址1
        "address2":"XXXXXX",#收件地址2 非必填,可替换成 " "
        "consigneeCode":"03100",#收件人-邮编 必须为5-6位数字。对收件人邮编进行匹配。如果邮编有误则报错，请客户确认该邮编是否存在。 例如：03100
    },#收件信息
    "orderGoods":{
        "weight":1,#包裹预报重量，单位：kg，值为0.001-99.00 例如：50
        "length":1,#包裹的长，单位：cm, 固定2位小数，若无则固定传1 例如：25   范围1到999
        "height":1,#包裹的高，单位：cm, 固定2位小数，若无则固定传1 例如：5  范围1到999
        "width":1,#包裹的宽，单位：cm, 固定2位小数，若无则固定传1 例如：10  范围1到999
    },#订单货物规格
    "orderItemList":[
        {
        "itemNameEn":"XXXX",    # itemNameEn:string 物品名称长度1-128
        "itemName":"连衣裙",     # 非必填 itemNameZh:string 物品中文名称 例如：连衣裙长度1-60
        "quantity":1            # itemQty:number  物品件数 例如：1 范围1到9999
    },
        {
        "itemNameEn": "XXXX",  # itemNameEn:string 物品名称长度1-128
        "itemName": "连衣裙",  # 非必填 itemNameZh:string 物品中文名称 例如：连衣裙长度1-60
        "quantity": 1  # itemQty:number  物品件数 例如：1 范围1到9999
    },
    ],#订单物品信息
    "queryCollectStartTime":"2025-03-03 08:00:00" ,#揽收开始时间 标准格式：yyyy-MM-dd HH:mm:ss
    "queryCollectEndTime":"2025-03-03 18:59:59" #揽收开始时间 标准格式：yyyy-MM-dd HH:mm:ss
}

response=requests.post(url=url,headers=header,data=data)
print(response.text)