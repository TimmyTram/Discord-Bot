import websockets
import asyncio
from dotenv import load_dotenv
import os

async def get_llm_response(prompt, context_id):
    uri = f'ws://{os.getenv('SERVER_HOST_NAME')}:{os.getenv('SERVER_PORT')}'
    async with websockets.connect(uri) as websocket:
        await websocket.send(prompt)
        response = await websocket.recv()
        return response