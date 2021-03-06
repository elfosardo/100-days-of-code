import argparse
import socket
import time

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 50000
BUFFER = 1024


def get_arguments():
    parser = argparse.ArgumentParser(description='File Transfer Client')
    parser.add_argument('myfile', metavar='F',
                        help='file to transfer')
    parser.add_argument('--host', dest='hostname', default=DEFAULT_HOST,
                        help='server hostname or ip; default to localhost')
    parser.add_argument('-p', '--port', dest='port', default=DEFAULT_PORT,
                        help='connection port; default 50000')
    arguments = parser.parse_args()
    return arguments


def send_file():
    my_file_to_send = open(args.myfile, 'rb')
    data_to_send = my_file_to_send.read(BUFFER)
    while data_to_send:
        my_socket.send(data_to_send)
        data_to_send = my_file_to_send.read(BUFFER)
    my_file_to_send.close()
    return True


if __name__ == '__main__':
    args = get_arguments()
    host = args.hostname
    filename = args.myfile + '\n'
    print('connecting')
    my_socket = socket.socket()
    my_socket.connect((host, args.port))
    my_socket.send(filename.encode())
    time.sleep(1)
    send_file()
    print('File successfully sent')
    my_socket.close()
    print('Connection closed')
