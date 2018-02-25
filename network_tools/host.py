import paramiko
import subprocess


class Host:
    def __init__(self, ip_address):
        self.hostname = ''
        self.ip_address = ip_address
        self.is_alive = False
        self.uptime = ''
        self.open_ports = []
        self.binary_ip_address = ''
        self.ssh_connection = None

    def ping_host(self):
        try:
            subprocess.check_output(["ping", "-c", "2", self.ip_address])
        except:
            return False
        return True

    def get_is_alive(self):
        self.is_alive = self.ping_host()
        return self.is_alive

    def get_uptime(self, username, password):
        self.uptime = self.execute_remote_command(username=username, password=password, remote_command='uptime')
        return self.uptime

    def execute_remote_command(self, username, password, remote_command):
        self.connect_to_host(username=username, password=password)
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh_connection.exec_command(remote_command)
        command_output = ssh_stdout.readlines()
        return command_output

    def connect_to_host(self, username, password):
        ssh_connection = paramiko.SSHClient()
        ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connection.connect(self.ip_address, username=username, password=password)
        self.ssh_connection = ssh_connection
        return self.ssh_connection

    def close_ssh_connection(self):
        self.ssh_connection.close()
        return True
