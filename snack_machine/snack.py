class Snack:
    """
    This class represents a single snack
    """
    name = ""
    price = 0.0
    amount = 0

    def __init__(self, name: str, price: float, amount: int):
        if not isinstance(name, str):
            raise TypeError("'Snack.name' was not 'string'")
        if not isinstance(price, float):
            raise TypeError("'Snack.price' was not 'float'")
        if not isinstance(amount, int):
            raise TypeError("'Snack.amount' was not 'int'")

        self.name = name
        self.price = price
        self.amount = amount

    def buy(self) -> bool:
        """
        This method deducts 1 from the product amount
        as long as the snack is in stock
        :return: True, if the process was successful
                 False, if the process could not be completed
        """
        if self.amount > 0:
            self.amount -= 1
            return True
        return False


