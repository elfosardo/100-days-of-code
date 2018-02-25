import argparse
from host import Host


def generate_arguments():
    parser = argparse.ArgumentParser(description='Connect to a host and reports the uptime')
    parser.add_argument('host', metavar='H', help='host to connect to')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = generate_arguments()

    my_host = Host(ip_address=args.host)

    result = my_host.get_uptime()

    print(' '.join(result))

    my_host.close_ssh_connection()
