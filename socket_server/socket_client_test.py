import socket

my_socket = socket.socket()
host = socket.gethostname()
port = 12345

my_socket.connect((host, port))
print(my_socket.recv(1024))
my_socket.close()
