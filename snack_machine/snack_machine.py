import os
from snack import Snack
from tui_engine import TuiEngine
from exceptions import InvalidInputError,\
                       BalanceToLowError,\
                       ItemNotInStockError


def display_error(message: str):
    """
    Displays an error message and forces the user to confirm.

    :param message: The message to be displayed
    :return: None
    """
    print(message)
    input("Press 'enter' to continue...")


class SnackMachine:
    """
    Simulates a snack-machine.
    """
    balance = 0.0
    selected_index = 0
    snacks = []
    engine = TuiEngine()

    def __init__(self, balance: float):
        if not isinstance(balance, float):
            raise TypeError("'SnackMachine.balance' was not 'float'")

        self.balance = balance
        self._generate_snacks()
        self.display()

    def _generate_snacks(self):
        """
        Creates a list of snacks.

        :return: None
        """
        snickers = Snack("Snickers          ", 0.85, 2)
        mars = Snack("Mars              ", 1.00, 2)
        lays = Snack("Lays Chips        ", 1.25, 2)
        milky = Snack("Milky Chocolate   ", 0.80, 2)
        gummybears = Snack("Gummybears        ", 1.05, 2)
        gum = Snack("Gum (5x Pieces)   ", 0.50, 2)
        potato = Snack("A singular potato ", 0.23, 2)
        cookies = Snack("Oreo Cookies      ", 0.95, 2)
        hypercube = Snack("A Hypercube. What?", 10.00, 2)
        bounty = Snack("Bounty            ", 0.90, 2)

        self.snacks.append(snickers)
        self.snacks.append(mars)
        self.snacks.append(lays)
        self.snacks.append(milky)
        self.snacks.append(gummybears)
        self.snacks.append(gum)
        self.snacks.append(potato)
        self.snacks.append(cookies)
        self.snacks.append(hypercube)
        self.snacks.append(bounty)

    def run(self):
        """
        The 'main' loop of the application.\n
        Takes care of error handling.

        :return: None
        """
        while True:
            try:
                self.display()
                self.handle_input()
            except TypeError:
                display_error("There has been an error while trying to read a value.")
            except ValueError:
                display_error("Invalid Input.")
            except IndexError:
                display_error("Item not for sale.")
            except BalanceToLowError:
                display_error("You do not have enough money.")
            except ItemNotInStockError:
                display_error("This item is currently not in stock.")

    def handle_input(self):
        """
        Handles the users input and calls the\n
        corresponding methods

        :return: None
        """
        option = input("Input: ")

        if option == "q":
            exit(0)

        elif option == "b":
            self.add_balance()

        elif option.isnumeric():
            buy_index = int(option)
            self.buy_snack(buy_index)

        else:
            raise InvalidInputError()

    def buy_snack(self, index: int):
        """
        Handles the 'buying' process of the machine.

        :param index: The index of the item to buy
        :return: None
        """
        if self.snacks[index].price > self.balance:
            raise BalanceToLowError()

        if not self.snacks[index].buy():
            raise ItemNotInStockError

        self.balance -= self.snacks[index].price

    def add_balance(self):
        """
        This method enables the user to add balance to the snack machine.

        :return: None
        """
        os.system("clear")

        added_balance = float(input("Amount: ").replace("b", "").strip())
        self.balance += added_balance

    def display(self):
        """
        Formats the object's data for TuiEngine.
        Then runs TuiEngine.render().

        :return: None
        """
        title = "Snack Machine"
        infos = {"Balance": f"{self.balance:.2f}€",
                 "Add balance   ": "Enter 'b'",
                 "Buy an item   ": "Enter item id",
                 "Exit          ": "Enter 'q'"}

        options = []
        for index, snack in enumerate(self.snacks):
            if snack.amount > 0:
                options.append(f"{index} | {snack.name} ({snack.amount}x): {snack.price:.2f}€")

        self.engine.render(title=title, data=infos, options=options)
