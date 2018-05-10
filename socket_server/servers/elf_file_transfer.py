import argparse
import threading
import server_config as sc
import file_transfer_server as fts

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Transfer Server')
    parser.add_argument('-p', '--port', dest='port', default=sc.DEFAULT_PORT,
                        help='connection port; default 50000')
    args = parser.parse_args()

    my_address = (sc.HOST, args.port)
    server = fts.MyFileServer(my_address, fts.MyFileServerHandler)
    new_thread = threading.Thread(target=server.serve_forever(), daemon=True)
    new_thread.start()
