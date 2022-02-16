from exceptions import InvalidArgumentException


def dict_line_length(element: dict) -> int:
    """
    Calculates the length of the longest key/value-pair in a dictionary.\n
    The length will be calculated from this format:\n
    "<key>: <value>".

    :param element: The dictionary the calculation will be performed on.
    :return:
    """
    element_len = 0
    for key, entry in element.items():
        line_len = len(f"{key}: {entry}")
        element_len = max(element_len, line_len)

    return element_len


def list_line_length(element: list):
    """
    Calculates the length of the longest entry in a list.

    :param element: The list the calculation will be performed on.
    :return:
    """
    element_len = 0
    for entry in element:
        line_len = len(entry)
        element_len = max(element_len, line_len)

    return element_len


def check_args(*args):
    """
    Checks if any parameter is None.\n
    Throws InvalidArgumentException if yes.

    :param args:
    :return:
    """
    for arg in args:
        if arg is None:
            raise InvalidArgumentException("A parameter was 'None'.")
