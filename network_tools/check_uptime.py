import argparse
import getpass
import paramiko

REMOTE_COMMAND = 'uptime'


def connect_to_host(hostname, username, password):
    ssh_connection = paramiko.SSHClient()
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connection.connect(hostname, username=username, password=password)
    return ssh_connection


def execute_remote_command(ssh_connection):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_connection.exec_command(REMOTE_COMMAND)
    command_output = ssh_stdout.readlines()
    return command_output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Connect to a host and reports the uptime')
    parser.add_argument('username', metavar='username',
                        help='username used to connect')
    parser.add_argument('hostname', metavar='hostname',
                        help='the host we want to connect to')
    args = parser.parse_args()

    my_password = getpass.getpass()

    my_ssh_connection = connect_to_host(args.hostname, args.username, my_password)

    result = execute_remote_command(my_ssh_connection)

    print(' '.join(result))

    my_ssh_connection.close()
