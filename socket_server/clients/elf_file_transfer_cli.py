import argparse
import socket

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Transfer Client')
    parser.add_argument('myfile', metavar='F',
                        help='file to transfer')
    parser.add_argument('-p', '--port', dest='port', default=50000,
                        help='connection port; default 50000')
    args = parser.parse_args()

    my_socket = socket.socket()
    host = socket.gethostname()

    my_socket.connect((host, args.port))
    my_socket.send('Hey server!'.encode())

    my_file_to_send = open(args.myfile, 'rb')
    data_to_send = my_file_to_send.read(1024)
    while data_to_send:
        my_socket.send(data_to_send)
        data_to_send = my_file_to_send.read(1024)
    my_file_to_send.close()

    print('File successfully sent')
    my_socket.close()
    print('Connection closed')
