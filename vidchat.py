from vidstream import *
import threading
import time
import socket

LOCAL_IP = socket.gethostbyname(socket.gethostname())
print(f"Local IP address is {LOCAL_IP}")

recv = StreamingServer(LOCAL_IP,9999)
send = CameraClient(LOCAL_IP,8888)

t1 = threading.Thread(target=recv.start_server)
t1.start()

time.sleep(2)

t2 = threading.Thread(target=send.start_stream)
t2.start()

while input("") != "stop":
    continue

recv.stop_server()
send.stop_stream()