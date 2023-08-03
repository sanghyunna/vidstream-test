import socket
import threading

# Code for PC

TARGET_BLUETOOTH_ADDRESS = "E4:5F:01:AF:D7:8E" # Rpi MAC address
RFCOMM_PORT = 1
SOCKET_IS_RUNNING = False

client_sock = socket.socket(
    socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
)

print(f"Attempting to connect to {TARGET_BLUETOOTH_ADDRESS} on RFCOMM channel {RFCOMM_PORT}")
client_sock.connect((TARGET_BLUETOOTH_ADDRESS, RFCOMM_PORT))
print(f"Connected to {TARGET_BLUETOOTH_ADDRESS} on RFCOMM channel {RFCOMM_PORT}")
SOCKET_IS_RUNNING = True

def readingThreadFunc(client_sock):
    while SOCKET_IS_RUNNING:
        try:
            text_data = client_sock.recv(1024)
            print(text_data.decode("utf-8"))
        except:
            client_sock.close()
            print("Connection closed")
            break

# def sendingThreadFunc(client_sock):
#     while True:
#         input_data = input("Send > ")
#         if input_data == "stop":
#             break
#         client_sock.send(input_data.encode("utf-8"))

readingThread = threading.Thread(target=readingThreadFunc, args=(client_sock,))
# sendingThread = threading.Thread(target=sendingThreadFunc, args=(client_sock,))

readingThread.start()

try:
    while SOCKET_IS_RUNNING:
        input_data = input()
        if input_data == "stop":
            client_sock.close()
            print("Connection closed")
            SOCKET_IS_RUNNING = False
            break
        input_data = "PC > " + input_data
        client_sock.send(input_data.encode("utf-8"))
except:
    client_sock.close()
    print("Exception : Connection closed")
     

