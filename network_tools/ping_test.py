import argparse
import subprocess


def ping_host(host):
    try:
        subprocess.check_output(["ping", "-c", "2", host])
    except:
        return False

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ping Host')
    parser.add_argument('host', metavar='H', help='host to ping')

    args = parser.parse_args()

    if ping_host(args.host):
        print('Host is alive!')
    else:
        print('Host looks dead')
