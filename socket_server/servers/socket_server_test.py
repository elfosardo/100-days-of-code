import socket

my_socket = socket.socket()
host = socket.gethostname()
port = 12345
my_socket.bind((host, port))

my_socket.listen(5)
while True:
    (my_connection, addr) = my_socket.accept()
    print('Got connection from', addr)
    msg = 'Connection accepted'.encode()
    my_connection.sendall(msg)
    my_connection.close()
