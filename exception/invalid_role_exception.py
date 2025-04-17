class InvalidRoleException(Exception):
    def __init__(self, message="Invalid role specified. Allowed roles are 'admin' and 'user'."):
        super().__init__(message)
