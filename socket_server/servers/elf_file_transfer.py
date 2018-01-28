import argparse
import socket


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Transfer Server')
    parser.add_argument('-p', '--port', dest='port', default=50000,
                        help='connection port; default 50000')
    args = parser.parse_args()

    my_socket = socket.socket()
    host = socket.gethostname()
    my_socket.bind((host, args.port))
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
