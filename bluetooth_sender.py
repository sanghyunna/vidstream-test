import socket

local_bluetooth_addr = "E4:5F:01:AF:D7:8E"  # Replace with your local Bluetooth address

server_sock = socket.socket(
    socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
)

server_sock.bind((local_bluetooth_addr, 1))
server_sock.listen(1)

print("Listening for connection on RFCOMM channel 1")

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

text_data = "Hello, Bluetooth!"
client_sock.send(text_data.encode("utf-8"))

client_sock.close()
server_sock.close()
