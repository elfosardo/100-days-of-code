import paramiko
import subprocess
from user import User


class Host:
    def __init__(self, ip_address, user_session=None):
        self.hostname = ''
        self.ip_address = ip_address
        self.is_alive = False
        self.uptime = ''
        self.open_ports = []
        self.binary_ip_address = ''
        self.ssh_connection = None
        self.user_session = user_session

    def __ping_host(self):
        try:
            subprocess.check_output(["ping", "-c", "2", self.ip_address])
        except:
            return False
        return True

    def get_is_alive(self):
        self.is_alive = self.__ping_host()

    def get_uptime(self):
        uptime = self.execute_remote_command(remote_command='uptime')
        self.uptime = ' '.join(uptime)

    def execute_remote_command(self, remote_command):
        if self.ssh_connection is None:
            self.connect_to_host()
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh_connection.exec_command(remote_command)
        command_output = ssh_stdout.readlines()
        return command_output

    def connect_to_host(self):
        if self.user_session is None:
            user_session = User()
        ssh_connection = paramiko.SSHClient()
        ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connection.connect(self.ip_address,
                               username=user_session.username,
                               password=user_session.password)
        self.ssh_connection = ssh_connection

    def close_ssh_connection(self):
        self.ssh_connection.close()
