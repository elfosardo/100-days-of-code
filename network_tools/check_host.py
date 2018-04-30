import argparse
from host import Host


def generate_arguments():
    parser = argparse.ArgumentParser(description='Collect information'
                                                 'about a host')
    parser.add_argument('host', metavar='H', help='host to check')
    parser.add_argument('--ping', '-p', dest='ping', action='store_true',
                        help='ping the host')
    parser.add_argument('--uptime', '-u', dest='uptime', action='store_true',
                        help='reports uptime of the host')
    parser.add_argument('--scan_ports', '-s', dest='ports', type=str,
                        help='comma separated list of ports to scan')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = generate_arguments()
    my_host = Host(ip_address=args.host)

    if args.ping:
        my_host.set_status()

    if args.uptime:
        my_host.set_uptime()

    if len(args.ports) != 0:
        ports = args.ports.split(',')
        my_host.scan_ports(ports)

    my_host.show_host_status()

    my_host.close_ssh_connection()
