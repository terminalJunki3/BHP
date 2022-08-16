import socket

host = "192.168.1.1"
port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# send some data
client.connect((host, port))

# receive data
data, addr = client.recvfrom(4096)

print(data)
client.close()
