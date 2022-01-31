# pip install sockets
# @author: KhomZ

import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print("Your Device name is: ", hostname)
print("Your Device's IP Address is: ", IP)
