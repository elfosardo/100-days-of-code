import argparse
from host import Host


def generate_arguments():
    parser = argparse.ArgumentParser(description='Ping Host')
    parser.add_argument('host', metavar='H', help='host to ping')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = generate_arguments()

    my_host = Host(ip_address=args.host)

    if my_host.get_is_alive():
        print('{} is alive!'.format(args.host))
    else:
        print('{} is dead...'.format(args.host))
