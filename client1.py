import time

import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


a = 0
b = time.time()


@sio.event
async def my_message(data):
    global a
    a = a + 1
    print('client received with ', data)
    await sio.emit('my_message1', {'response': a, "time": time.time() - b})


@sio.event
def my_message_all(data):
    global a
    a = a + 1
    print('client my_message_all received with ', data)
    # sio.emit('my_message1', {'response': a, "time":time.time()-b})


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:8000', auth={
    "auth1111": "au1111"
})
for i in range(3):
    print(i)

    sio.emit("my_message_all", f"aaaa{i}")
    input()
# sio.wait()
