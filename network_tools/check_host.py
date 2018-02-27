import argparse
from host import Host


def generate_arguments():
    parser = argparse.ArgumentParser(description='Collect information about a host')
    parser.add_argument('host', metavar='H', help='host to check')
    parser.add_argument('--ping', '-p', dest='ping', action='store_true',
                        help='ping the host')
    parser.add_argument('--uptime', '-u', dest='uptime', action='store_true',
                        help='reports uptime of the host')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = generate_arguments()
    my_host = Host(ip_address=args.host)

    if args.ping:
        my_host.set_status()

    if args.uptime:
        my_host.set_uptime()

    my_host.show_host_status()

    my_host.close_ssh_connection()
