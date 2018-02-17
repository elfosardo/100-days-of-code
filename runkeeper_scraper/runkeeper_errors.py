
class Error(Exception):
    pass


class AuthenticationFailed(Error):
    def __init__(self):
        self.message = 'Cookie not generated. Wrong Password?'

    def __str__(self):
        return self.message


class ConnectionFailed(Error):
    def __init__(self, url):
        self.message = 'URL {} not reachable'.format(url)

    def __str__(self):
        return self.message


class NoActivitiesFound(Error):
    def __init__(self, month, year):
        self.message = 'No activities found in {}/{}'.format(month, year)

    def __str__(self):
        return self.message
