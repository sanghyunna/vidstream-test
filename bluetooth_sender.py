import socket
import threading

# Code for Raspberry Pi

LOCAL_BLUETOOTH_ADDRESS = "E4:5F:01:AF:D7:8E" # Rpi MAC address
RFCOMM_PORT = 1

server_sock = socket.socket(
    socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
)

server_sock.bind((LOCAL_BLUETOOTH_ADDRESS, RFCOMM_PORT))
server_sock.listen(1)

print(f"Listening for connection on RFCOMM channel {RFCOMM_PORT}")

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

def readingThreadFunc(client_sock):
    while True:
        try:
            text_data = client_sock.recv(1024)
            print(text_data.decode("utf-8"))
        except:
            client_sock.close()
            server_sock.close()
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
    while True:
            input_data = input()
            if input_data == "stop":
                client_sock.close()
                server_sock.close()
                print("Connection closed")
                break
            input_data = "Raspi > " + input_data
            client_sock.send(input_data.encode("utf-8"))
except:
    client_sock.close()
    server_sock.close()
    print("Connection closed")
