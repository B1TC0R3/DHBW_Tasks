"""
The entry point of the application.
"""
from snack_machine import SnackMachine


def main():
    """
    The main method of the application.

    :return: None
    """
    snack_machine = SnackMachine(balance=0.0)
    snack_machine.run()


if __name__ == "__main__":
    main()
