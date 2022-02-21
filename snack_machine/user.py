class User:
    """
    Represents an account
    """
    def __init__(self, code: str, balance: str):
        self.code = code
        self.balance = float(balance)
