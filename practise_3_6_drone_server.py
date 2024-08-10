# pip install websockets asyncio
#
import websockets, asyncio


async def control_drone(websocket, path):
    try:
        async for msg in websocket:
                print(f"Received from client: {msg}")
                if msg == 'takeoff':
                    print('Drone is taking off')
                    await websocket.send('Drone is taking off')
                if msg == 'land':
                    print('Drone is landing')
                    await websocket.send('Drone is landing')
    except websockets.ConnectionClosedError as e:
        print(f"Client disconnected. {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


print("Starting WebSocket server...")
# создаем сервер с адресом и портом
# control_drone - ссылка на функцию
start_server = websockets.serve(control_drone, "localhost", 8765)
# запускаем сервер
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
print("WebSocket server started")
