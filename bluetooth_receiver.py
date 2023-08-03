import socket

target_bluetooth_addr = "E4:5F:01:AF:D7:8E"  # Replace with your server's Bluetooth address

client_sock = socket.socket(
    socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
)

print("Attempting to connect to %s on RFCOMM channel 1" % target_bluetooth_addr)
client_sock.connect((target_bluetooth_addr, 1))
print("Connected. Receiving data...")

text_data = client_sock.recv(1024)
print("Received:", text_data.decode("utf-8"))

client_sock.close()
