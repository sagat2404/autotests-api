import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        print(f"Получено сообщение от пользователя: {message}")
        await websocket.send(message)  # Отправляем сообщение

        for _ in range(5):
            message = await websocket.recv()
            print(f'1 Сообщение пользователя: {message}')
            print(f'2 Сообщение пользователя: {message}')
            print(f'3 Сообщение пользователя: {message}')
            print(f'4 Сообщение пользователя: {message}')
            print(f'5 Сообщение пользователя: {message}')


asyncio.run(client())
