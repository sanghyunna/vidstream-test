from vidstream import *

import socket
import threading

LOCAL_IP = socket.gethostbyname(socket.gethostname())
print(f"Local IP address is {LOCAL_IP}")

SENDER_OUTBOUND_PORT = 6666
RECIEVER_INBOUND_PORT = 7777
port_in = 0
port_out = 0


def set_to_sender_mode():
    port_in = 0 # Not used
    port_out = SENDER_OUTBOUND_PORT

def set_to_reciever_mode():
    port_in = RECIEVER_INBOUND_PORT
    port_out = 0 # Not used



server = StreamingServer(LOCAL_IP,port_in)
camera_client = None

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t1.start()

def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'), port_out)
    t2 = threading.Thread(target=camera_client.start_stream)
    t2.start()

def stop_everything():
    server.stop_server()
    camera_client.stop_stream()


# GUI Controller
import tkinter as tk
window = tk.Tk()
window.title("Video Transmission Control Panel")
window.geometry('300x400')

current_ip_string = "Current IP: " + LOCAL_IP

label_current_ip = tk.Label(window, text=current_ip_string)
label_current_ip.pack(anchor=tk.CENTER, expand=True)

label_target_ip = tk.Label(window, text='Target IP:')
label_target_ip.pack(anchor=tk.CENTER, expand=True)

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack(anchor=tk.CENTER, expand=True)

btn_set_sender = tk.Button(window, text='Sender Mode', width=50, command=set_to_sender_mode)
btn_set_sender.pack(anchor=tk.CENTER, expand=True)

btn_set_reciever = tk.Button(window, text='Reciever Mode', width=50, command=set_to_reciever_mode)
btn_set_reciever.pack(anchor=tk.CENTER, expand=True)

btn_listen = tk.Button(window, text='Start Listening', width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text='Start Sending Camera', width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_stop = tk.Button(window, text='Stop', width=50, command=stop_everything)
btn_stop.pack(anchor=tk.CENTER, expand=True)



window.mainloop()