import getpass


class User:
    def __init__(self, username=None, password=None):
        self.username = self.get_username(username)
        self.password = self.get_password(password)

    @staticmethod
    def get_username(username):
        if username is None:
            username = input('Type your username: ')
        return username

    @staticmethod
    def get_password(password):
        if password is None:
            password = getpass.getpass()
        return password
