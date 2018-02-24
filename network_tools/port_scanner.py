import argparse
import socket


def portscanner(host, port):
    test_port = my_socket.connect_ex((host, int(port)))
    return test_port


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple port scanner implementation')
    parser.add_argument('host', help='host to scan')
    parser.add_argument('port', help='port to scan')
    parser.add_argument('--timouet', '-t', dest='timeout', default=5,
                        help='Connection timeout; default to 5s')
    args = parser.parse_args()

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.settimeout(int(args.timeout))

    my_test = portscanner(args.host, args.port)

    if my_test == 0:
        print('Port {} on {} is open'.format(args.port, args.host))
    else:
        print('Port {} on {} is closed'.format(args.port, args.host))
