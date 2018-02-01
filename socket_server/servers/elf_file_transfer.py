import argparse
import socketserver

HOST = 'localhost'
DEFAULT_PORT = 50000
BUFFER = 1024


class MyFileServer(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(BUFFER)
        print(self.data)
        print('Connection received')
        received_file_name = (self.data.decode()).splitlines()[0]
        print('Receiving file: ', received_file_name)
        with open(received_file_name, 'wb') as received_file:
            print('Upload started')
            while True:
                print('Receiving data...')
                self.data = self.request.recv(BUFFER)
                if not self.data:
                    break
                received_file.write(self.data)
        received_file.close()
        print('Done receiving')
        self.request.sendall('Data received'.encode())
        self.request.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Transfer Server')
    parser.add_argument('-p', '--port', dest='port', default=DEFAULT_PORT,
                        help='connection port; default 50000')
    args = parser.parse_args()

    server = socketserver.TCPServer((HOST, args.port), MyFileServer)

    print('Server listening...')

    server.serve_forever()
