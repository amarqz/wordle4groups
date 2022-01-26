class Error(Exception):
    pass

class AlreadyIn(Error):
    """Raised when the sent result for a certain day is already registered."""
    pass