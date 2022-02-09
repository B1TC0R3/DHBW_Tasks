class InvalidLoginException(Exception):
    def __init__(self):
        super(InvalidLoginException, self).__init__()


class AccountExistsException(Exception):
    def __init__(self):
        super(AccountExistsException, self).__init__()


class InvalidArgumentException(Exception):
    def __init__(self):
        super(InvalidArgumentException, self).__init__()


class BalanceToLowException(Exception):
    def __init__(self):
        super(BalanceToLowException, self).__init__()


class InvalidTransferAmountException(Exception):
    def __init__(self):
        super(InvalidTransferAmountException, self).__init__()


class RecipientNotFoundException(Exception):
    def __init__(self):
        super(RecipientNotFoundException, self).__init__()
