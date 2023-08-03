from vidstream import *
import threading
# import time
# import socket
import os

# LOCAL_IP = socket.gethostbyname(socket.gethostname())
LOCAL_IP = os.popen("ip -4 route show default").read().split()[8]
print(f"Local IP address is {LOCAL_IP}")

# recv = StreamingServer('192.168.0.88',8888)
send = CameraClient('192.168.0.67',9999)

# t1 = threading.Thread(target=recv.start_server)
# t1.start()

# time.sleep(2)

t2 = threading.Thread(target=send.start_stream)
t2.start()

while input("") != "stop":
    continue

# recv.stop_server()
send.stop_stream()