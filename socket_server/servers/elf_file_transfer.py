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
        self.logger.debug('Closing File')
        received_file.close()
        self.logger.debug('Done receiving')
        self.request.close()
        return


class MyFileServer(socketserver.TCPServer):

    def __init__(self, server_address, handler_class=MyFileServerHandler):
        self.logger = logging.getLogger('MyFileServer')
        self.logger.debug('__init__')
        self.logger.debug('Server listening...')
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        return

    def serve_forever(self):
        self.logger.debug('Waiting connection requests')
        self.logger.info('Handling requests, press <Ctrl-C> to quit')
        socketserver.TCPServer.serve_forever(self)
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return socketserver.TCPServer.handle_request(self)


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

    my_address = (HOST, args.port)
    server = MyFileServer(my_address, MyFileServerHandler)
    new_thread = threading.Thread(target=server.serve_forever(), daemon=True)
    new_thread.start()
