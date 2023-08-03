import socket

server_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

port = 3
server_sock.bind(("", port))
server_sock.listen(1)

print("Waiting for connection...")

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

data = client_sock.recv(1024)  # Adjust buffer size as needed
print(f"Received: {data.decode()}")

client_sock.close()
server_sock.close()
