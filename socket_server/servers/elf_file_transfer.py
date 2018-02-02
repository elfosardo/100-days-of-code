import argparse
import logging
import socketserver
import threading

HOST = 'localhost'
DEFAULT_PORT = 50000
BUFFER = 1024


class MyFileServerHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('MyFileServerHandler')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(self, request,
                                                 client_address,
                                                 server)
        return

    def handle(self):
        self.data = self.request.recv(BUFFER)
        self.logger.debug('Connection received')
        received_file_name = (self.data.decode()).splitlines()[0]
        self.logger.debug('Receiving file: %s', received_file_name)
        with open(received_file_name, 'wb') as received_file:
            self.logger.debug('Upload started')
            while True:
                self.logger.debug('Receiving data...')
                self.data = self.request.recv(BUFFER)
                if not self.data:
                    break
                received_file.write(self.data)
        received_file.close()
        self.logger.debug('Done receiving')
        self.request.sendall('Data received'.encode())
        self.request.close()
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Transfer Server')
    parser.add_argument('-p', '--port', dest='port', default=DEFAULT_PORT,
                        help='connection port; default 50000')
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S',
        format='%(asctime)s (%(threadName)-10s) %(name)s: %(message)s',
    )

    server_address = (HOST, args.port)
    server = socketserver.TCPServer(server_address, MyFileServerHandler)
    logging.debug('Server listening...')
    new_thread = threading.Thread(target=server.serve_forever(), daemon=True)
    new_thread.start()
