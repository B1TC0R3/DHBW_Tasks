from exceptions import InvalidArgumentException


def check_args(*args):
    for arg in args:
        if arg is None:
            raise InvalidArgumentException("A parameter was 'None'.")


check_args(None)
