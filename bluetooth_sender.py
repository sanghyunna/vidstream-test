import socket
import time

server_address = "E4:5F:01:AF:D7:8E"  # Replace with the receiver's Bluetooth address
port = 3
text = "Hello, Bluetooth!"

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock.connect((server_address, port))

time.sleep(2)  # Give some time for the connection to be established

sock.send(text.encode())
print(f"Sent: {text}")

sock.close()
