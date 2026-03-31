import asyncio
import sys
import websockets

async def send_message(message):
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received: {response}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python client.py <message>")
        sys.exit(1)

    message = sys.argv[1]
    asyncio.run(send_message(message))