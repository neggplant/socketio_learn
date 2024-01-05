import time

import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
a = 0
b = time.time()
@sio.event
def my_message(data):
    global a
    a=a+ 1
    print('client received with ', data)
    sio.emit('my_message1', {'response': a, "time":time.time()-b})

@sio.event
def my_message_all(data):
    global a
    a=a+ 1
    print('client my_message_all received with ', data)
    # sio.emit('my_message_all', {'response': a, "time":time.time()-b})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:8001')
for i in range(3):
    print(i)

    sio.emit("my_message", f"aaaa{i}")
    input()
# sio.wait()