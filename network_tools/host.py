import paramiko
import socket
import subprocess
from user import User


class Host:
    def __init__(self, ip_address, user_session=None):
        self.hostname = ''
        self.ip_address = ip_address
        self.status = 'Down'
        self.uptime = ''
        self.open_ports = []
        self.binary_ip_address = ''
        self.__ssh_connection = None
        self.__user_session = user_session

    def __ping_host(self):
        try:
            subprocess.check_output(["ping", "-c", "2", self.ip_address])
        except:
            return False
        return True

    def set_status(self):
        if self.__ping_host():
            self.status = 'UP'

    def __get_uptime(self):
        list_uptime = self.execute_remote_command(remote_command='uptime')
        uptime = ' '.join(list_uptime).rstrip('\n')
        return uptime

    def set_uptime(self):
        self.uptime = self.__get_uptime()

    def execute_remote_command(self, remote_command):
        if self.__ssh_connection is None:
            self.connect_to_host()
        ssh_stdin, ssh_stdout, ssh_stderr = self.__ssh_connection.exec_command(remote_command)
        command_output = ssh_stdout.readlines()
        return command_output

    def connect_to_host(self):
        if self.__user_session is None:
            user_session = User()
        ssh_connection = paramiko.SSHClient()
        ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connection.connect(self.ip_address,
                               username=user_session.username,
                               password=user_session.password)
        self.__ssh_connection = ssh_connection

    @staticmethod
    def portscanner(host, port, timeout=1):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.settimeout(int(timeout))
        test_port = my_socket.connect_ex((host, int(port)))
        my_socket.close()
        return test_port

    def scan_ports(self, ports):
        for port in ports:
            my_test = self.portscanner(host=self.ip_address, port=port)
            if my_test == 0:
                self.open_ports.append(port)

    def close_ssh_connection(self):
        if self.__ssh_connection:
            self.__ssh_connection.close()
        return True

    def show_host_status(self):
        print('\nHost Status')
        print('hostname: {}'.format(self.hostname))
        print('ip address: {}'.format(self.ip_address))
        print('status: {}'.format(self.status))
        print('uptime: {}'.format(self.uptime))
        print('open ports: {}'.format(self.open_ports))
