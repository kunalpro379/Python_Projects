import asyncio
import websockets

clients={'male': set(), 'female': set()}

async def handle_clients(websocket, path):
    gender =await websocket.recv()#recieving gender 

    clients[gender].add(websocket)