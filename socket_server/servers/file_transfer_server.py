import logging
import socketserver
import server_config as sc


class MyFileServerHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('MyFileServerHandler')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(self, request,
                                                 client_address,
                                                 server)
        return

    def handle(self):
        self.data = self.request.recv(sc.BUFFER)
        self.logger.debug('Connection received')
        received_file_name = (self.data.decode()).splitlines()[0]
        self.logger.debug('Receiving file: %s', received_file_name)
        with open(received_file_name, 'wb') as received_file:
            self.logger.debug('Upload started')
            while True:
                self.logger.debug('Receiving data...')
                self.data = self.request.recv(sc.BUFFER)
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
