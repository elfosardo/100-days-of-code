import argparse
import binascii
import ipaddress


def convert_to_integer():
    int_ip_address = int(my_ip_address)
    return int_ip_address


def convert_to_binary(int_ip_address):
    binary_ip = ipaddress.v4_int_to_packed(int_ip_address)
    formatted_binary_ip = binascii.hexlify(binary_ip)
    decoded_ip = formatted_binary_ip.decode()
    return decoded_ip


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IP conversion tool')
    parser.add_argument('ip_address', help='IPv4 address to convert')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', action='store_true', dest='binary',
                       help='Convert to binary')
    group.add_argument('-i', action='store_true', dest='integer',
                       help='Convert to integer')

    args = parser.parse_args()

    my_ip_address = ipaddress.ip_address(args.ip_address)
    my_int_ip_address = convert_to_integer()

    converted_ip= ''

    if args.integer:
        converted_ip = my_int_ip_address

    if args.binary:
        converted_ip = convert_to_binary(my_int_ip_address)

    if not args.integer and not args.binary:
        print('You need to specify a type of conversion')
    else:
        print(converted_ip)
