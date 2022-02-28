"""
Contains the class account.
"""

class Account:
    """
    Its an account.
    """

    def __init__(self, name: str, pwd: str):
        self.name = name
        self.pwd = pwd
        self.balance = 0.0

    def add_balance(self, balance: float):
        """
        Adds a positiv ammount of money to the accounts balance.

        :returns: None
        """
        if balance > 0.0:
            self.balance += balance
        else:
            raise ValueError()

    def get_name(self) -> str:
        """
        This returns the name of the account.

        :returns: str
        """
        return self.name

    def get_pwd(self) -> str:
        """
        This returns the password of the account.

        :returns: str
        """
        return self.pwd

    def to_json(self) -> dict:
        """
        Converts the object to a dict serializable by json.

        :returns: dict
        """
        return {"name": self.name,
                "pwd": self.pwd,
                "balance": self.balance}
