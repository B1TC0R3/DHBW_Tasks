import snack


class SnackMachine:
    balance = 100.0
    items = []

    def __init__(self, balance: float):
        if type(balance) is not type(float):
            raise TypeError("'SnackMachine.balance' was not 'float'")

        self.balance = balance
        self._generate_snacks()

    def _generate_snacks(self):
        snickers = Snack("Snickers", 0.85, 2)
        mars = Snack("Mars", 1.00, 2)
        lays = Snack("Lays Chips", 1.25, 2)
        milky = Snack("Milky Chocolate", 0.80, 2)
        gummybears = Snack("Gummybears", 1.05, 2)
        gum = Snack("Gum (5x Pieces)", 0.50, 2)
        potato = Snack("A singular potato", 0.23, 2)
        cookies = Snack("Oreo Cookies", 0.95, 2)
        hypercube = Snack("A Hypercube. What?", 10.00, 2)
        bounty = Snack("Bounty", 0.90, 2)

        self.items.append(snickers)
        self.items.append(mars)
        self.items.append(lays)
        self.items.append(milky)
        self.items.append(gummybears)
        self.items.append(gum)
        self.items.append(potato)
        self.items.append(cookies)
        self.items.append(hypercube)
        self.items.append(bounty)

    def add_balance(self, balance: float):
        if type(balance) is not type(float):
            raise TypeError("'SnackMachine.balance' was not 'float'")

        self.balance += balance
