"""
Contains some custom exceptions.
This allows for more detailed error handling.
"""


class BalanceToLowError(Exception):
    """
    Error thrown when the user does not have enough balance to buy an item
    """


class InvalidInputError(Exception):
    """
    Error thrown when a user enters invalid strings for certain options
    """


class ItemNotInStockError(Exception):
    """
    Error thrown when the user tries to buy an item whose amount has reached zero
    """


class InvalidArgumentError(Exception):
    """
    An error thrown when a method/function receives an invalid parameter
    """
