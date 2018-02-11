

class Error(Exception):
    pass


class AuthenticationFailed(Error):
    def __init__(self, message):
        self.message = message