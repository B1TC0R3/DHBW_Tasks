from exceptions import InvalidArgumentException


def dict_line_length(element: dict) -> int:
    element_len = 0
    for key, entry in element.items():
        line_len = len(f"{key}: {entry}")
        element_len = max(element_len, line_len)

    return element_len


def list_line_length(element: list):
    element_len = 0
    for entry in element():
        line_len = len(entry)
        element_len = max(element_len, line_len)

    return element_len


def check_args(*args):
    for arg in args:
        if arg is None:
            raise InvalidArgumentException("A parameter was 'None'.")


if __name__ == "__main__":
    print("Testing 'check_args'\n"
          "Expected Result: throws InvalidArgumentException\n"
          "Actual result:\n")
    check_args(None)
