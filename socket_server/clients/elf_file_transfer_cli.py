import argparse
import socket

DEFAULT_PORT = 50000
BUFFER = 1024


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Transfer Client')
    parser.add_argument('myfile', metavar='F',
                        help='file to transfer')
    parser.add_argument('-p', '--port', dest='port', default=DEFAULT_PORT,
                        help='connection port; default 50000')
    args = parser.parse_args()

    my_socket = socket.socket()
    host = socket.gethostname()

    my_socket.connect((host, args.port))

    filename = args.myfile + '\n'
    my_socket.send(filename.encode())

    my_file_to_send = open(args.myfile, 'rb')
    data_to_send = my_file_to_send.read(BUFFER)
    while data_to_send:
        my_socket.send(data_to_send)
        data_to_send = my_file_to_send.read(BUFFER)
    my_file_to_send.close()

    print('File successfully sent')
    my_socket.close()
    print('Connection closed')
