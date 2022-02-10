class InvalidLoginException(Exception):
    def __init__(self):
        super(InvalidLoginException, self).__init__()


class AccountExistsException(Exception):
    def __init__(self):
        super(AccountExistsException, self).__init__()


class InvalidArgumentException(Exception):
    def __init__(self, msg: str):
        super(InvalidArgumentException, self).__init__(msg)


class BalanceToLowException(Exception):
    def __init__(self, msg: str):
        super(BalanceToLowException, self).__init__(msg)


class InvalidTransferAmountException(Exception):
    def __init__(self):
        super(InvalidTransferAmountException, self).__init__()


class RecipientNotFoundException(Exception):
    def __init__(self):
        super(RecipientNotFoundException, self).__init__()
