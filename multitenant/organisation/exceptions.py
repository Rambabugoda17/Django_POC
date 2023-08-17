class AuthorizationException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    pass


class InvalidEmailException(Exception):

    """Please provide valid email address"""
    def __init__(self, message="Invalid email address"):
        self.message = message
        super().__init__(self.message)

    pass
