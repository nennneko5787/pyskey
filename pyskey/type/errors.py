class UserNotAuthorizedError(Exception):
    def __init__(self, message="User is not authenticated."):
        self.message = message
        super().__init__(self.message)

class AuthorizeForbiddenError(Exception):
    def __init__(self, message="Login failed, either you do not have permission to access the API, you are not a misskey server, or you are incompatible with this version of Pyskey."):
        self.message = message
        super().__init__(self.message)

class AuthorizeNotFoundError(Exception):
    def __init__(self, message="Login failed. The address is not a misskey server or is incompatible with this version of Pyskey."):
        self.message = message
        super().__init__(self.message)

class RateLimitedError(Exception):
    def __init__(self, message="RateLimited"):
        self.message = message
        super().__init__(self.message)

class ClientError(Exception):
    def __init__(self, message="ClientError"):
        self.message = message
        super().__init__(self.message)