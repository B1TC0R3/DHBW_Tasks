class Account:
    """
    Represents an accounts
    """
    code: str
    balance: float

    def __int__(self, code: str, balance: str):
        self.code = code
        self.balance = float(balance)
