"""
Contains multiple simple calculations
and other functionality
"""
import hashlib
from exceptions import InvalidArgumentError


def get_hash(pwd: str, salt: str) -> str:
    """
    Wrapper method for hashlib.
    Calculates the hash from a string and a salt.

    :param pwd: The passwor to be hashed
    :param salt: The salt used to calculate the hash
    :returns: str
    """
    pwd_hash = hashlib.pbkdf2_hmac("sha256", bytes(pwd, "utf-8"), bytes(salt, "utf-8"), 100000)
    return pwd_hash.hex()


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
            raise InvalidArgumentError("A parameter was 'None'.")


if __name__ == "__main__":
    print("Running tests for 'utility.py'")

    # get_hash
    print("Testing 'get_hash':")
    print("\tHashing 'qwertz'")
    print(f"\tResult: {get_hash('qwertz', '12345')}")
    print("\tRepeating hash")
    print("\t->Result should be the same")
    print(f"\tResult: {get_hash('qwertz', '12345')}")
    print("\tTesting different salt")
    print(f"\tResult: {get_hash('qwertz', '54321')}")
    print("\n")
