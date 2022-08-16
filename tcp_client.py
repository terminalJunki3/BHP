import socket

target = "www.facebook.com"
port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to client
client.connect((target,port))
# Send data
client.send(b"GET / HTTP/1.1\r\nhost:google.com\r\n\r\r")
# Read Data
response = client.recv(4096)

print(response.decode())
client.close()

# Close connection