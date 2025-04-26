import asyncio

import execjs
import websockets




async def hello():
    uri = "wss://www.python-spider.com/api/challenge64"  # 替换为你的WebSocket服务器地址
    async with websockets.connect(uri) as websocket:
        await websocket.send(f"{1}")
        response = await websocket.recv()
        response = list(response)
        result = ''.join([chr(code) for code in response])

        print(f"Received: {result}")


asyncio.get_event_loop().run_until_complete(hello())