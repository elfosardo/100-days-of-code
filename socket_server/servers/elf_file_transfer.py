import socket

PORT = 50000

my_socket = socket.socket()
host = socket.gethostname()
my_socket.bind((host, PORT))
my_socket.listen(5)

print('Server listening...')

while True:
    (my_connection, addr) = my_socket.accept()
    print('Got connection from', addr)
    data = my_connection.recv(1024)
    print('Connection received')
    with open('received_file.txt', 'wb') as received_file:
        print('Upload started')
        while True:
            print('Receiving data...')
            data = my_connection.recv(1024)
            if not data:
                break
            received_file.write(data)
    received_file.close()

    print('Done receiving')
    my_connection.send('Data received'.encode())
    my_connection.close()
