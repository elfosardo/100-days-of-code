import socket

FILENAME = 'send_test.txt'
PORT = 50000

my_socket = socket.socket()
host = socket.gethostname()

my_socket.connect((host, PORT))
my_socket.send('Hey server!'.encode())

my_file_to_send = open(FILENAME, 'rb')
data_to_send = my_file_to_send.read(1024)
while data_to_send:
    my_socket.send(data_to_send)
    data_to_send = my_file_to_send.read(1024)
my_file_to_send.close()

print('File successfully sent')
my_socket.close()
print('Connection closed')
