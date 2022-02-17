class BalanceToLowError(Exception):
    def __init__(self, msg: str):
        super(BalanceToLowError, self).__init__(msg)


class InvalidInputError(Exception):
    def __init__(self):
        super(InvalidInputError, self).__init__()


class ItemNotInStockError(Exception):
    def __init__(self):
        super(ItemNotInStockError, self).__init__()
