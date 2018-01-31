import argparse
import socket

DEFAULT_PORT = 50000
BUFFER = 1024


def open_socket():
    my_socket = socket.socket()
    host = socket.gethostname()
    my_socket.bind((host, args.port))
    my_socket.listen(5)
    return my_socket


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Transfer Server')
    parser.add_argument('-p', '--port', dest='port', default=DEFAULT_PORT,
                        help='connection port; default 50000')
    args = parser.parse_args()

    new_socket = open_socket()

    print('Server listening...')

    while True:
        (my_connection, addr) = new_socket.accept()
        print('Got connection from', addr)
        data = my_connection.recv(BUFFER)
        print(data)
        print('Connection received')
        received_file_name = (data.decode()).splitlines()[0]
        print('Receiving file: ', received_file_name)
        with open(received_file_name, 'wb') as received_file:
            print('Upload started')
            while True:
                print('Receiving data...')
                data = my_connection.recv(BUFFER)
                if not data:
                    break
                received_file.write(data)
        received_file.close()

        print('Done receiving')
        my_connection.send('Data received'.encode())
        my_connection.close()
