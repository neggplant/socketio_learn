# server_socketio.py

# uvicorn server_socketio:socket_app --host 0.0.0.0 --port 8000
import socketio
from fastapi import FastAPI
from aiohttp import web


sio = socketio.AsyncServer(async_mode='asgi',client_manager=socketio.AsyncRedisManager('redis://:aa@localhost:6379/0'), cors_allowed_origins='*')
app = FastAPI()
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)


# 创建一个事件处理器，例如当客户端连接时
@sio.event
async def connect(sid, environ, auth=None):
    query_string = environ.get('auth')
    print('Client connected', sid, query_string, auth, environ)
    # return False


@sio.event
async def my_message(sid, data):
    print('message ', sid,data)
    await sio.emit('my_message', {'response': 'Message received!'}, to=sid)

@sio.event
async def my_message_all(sid, data):
    print('server_my_message_all ', sid,data)
    await sio.emit('my_message_all', {'response': 'Message received!', "data":data})

# 创建一个事件处理器，例如当客户端断开连接时
@sio.event
async def disconnect(sid):
    print('Client disconnected', sid)


# 使用 FastAPI 路由
@app.get("/")
async def read_root():
    return {"message": "Hello World from FastAPI"}

