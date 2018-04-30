import argparse
import ipaddress


def generate_arguments():
    parser = argparse.ArgumentParser(description='Give information about'
                                                 'a network')
    parser.add_argument('network',
                        help='specify a network with the format x.x.x.x/x for'
                             'ipv4 or x:x:x:x:x:x/x for ipv6')
    arguments = parser.parse_args()
    return arguments


def get_all_ip_addresses(network):
    all_ip_addresses = list(network.hosts())
    return all_ip_addresses


def get_first_ip_address(network):
    first_ip_address = get_all_ip_addresses(network)[0]
    return first_ip_address


def get_last_ip_address(network):
    last_ip_address = get_all_ip_addresses(network)[-1]
    return last_ip_address


if __name__ == '__main__':
    args = generate_arguments()

    my_network = ipaddress.ip_network(args.network)

    print('{!r}'.format(my_network))
    print('        is private:', my_network.is_private)
    print('  first ip address:', get_first_ip_address(my_network))
    print('   last ip address:', get_last_ip_address(my_network))
    print(' broadcast address:', my_network.broadcast_address)
    print(' compressed format:', my_network.compressed)
    print('      with netmask:', my_network.with_netmask)
    print('     with hostmask:', my_network.with_hostmask)
    print('   total addresses:', my_network.num_addresses)
