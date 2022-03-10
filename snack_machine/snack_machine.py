"""
Contains the main functionality of the project.
Includes error handling.
"""

import os
import sys
import json
from snack import Snack
from account import Account
from tui_engine import TuiEngine
from account_manager import create_account,\
                            login,\
                            save_account
from exceptions import InvalidInputError,\
                       BalanceToLowError,\
                       ItemNotInStockError,\
                       InvalidLoginError


def display_message(message: str):
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

    file_dir = "./save"
    file_snacks = "snacks.json"
    file_accounts = "accounts.json"

    def __init__(self, balance: float):
        if not isinstance(balance, float):
            raise TypeError("'SnackMachine.balance' was not 'float'")

        self.snacks = []
        self.engine = TuiEngine()
        self.active_acc = Account("None", "")

        if os.path.isfile(f"{self.file_dir}/{self.file_snacks}"):
            self._load_snacks()
        else:
            self._generate_snacks()
        self.display()

    def _load_snacks(self):
        """
        Loads snack data from save-file.

        :return:
        """
        with open(f"{self.file_dir}/{self.file_snacks}", "r", encoding="utf-8") as file:
            file_content = json.load(file)

            for snack in file_content:
                self.snacks.append(Snack(snack[0],
                                   float(snack[1]),
                                   int(snack[2])))

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

        self._save()

    def _restock(self):
        """
        Restores all snack data to the default.

        :returns: None
        """
        if os.path.isfile(f"{self.file_dir}/{self.file_snacks}"):
            os.system(f"rm {self.file_dir}/{self.file_snacks}")

        self.snacks.clear()
        self._generate_snacks()

    def _snacks_to_json(self) -> list:
        """
        Converts list of Snacks to a string\n
        readable by json

        :return: A two-dimensional list containing all the snacks data
        """
        json_snacks = []
        for snack in self.snacks:
            json_snacks.append([snack.name, str(snack.price), str(snack.amount)])

        return json_snacks

    def _save(self):
        """
        Save the machine's status to save-file

        :return: None
        """
        json_snacks = self._snacks_to_json()

        if not os.path.isdir(self.file_dir):
            os.mkdir(self.file_dir)

        access = "w" if os.path.isfile(f"{self.file_dir}/{self.file_snacks}") else "x"
        with open(f"{self.file_dir}/{self.file_snacks}", access, encoding="utf-8") as file:
            json.dump(json_snacks, file)

        save_account(self.active_acc)

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
                self._save()
            except TypeError:
                display_message("There has been an error while trying to read a value.")
            except ValueError:
                display_message("Invalid Input.")
            except IndexError:
                display_message("Item not for sale.")
            except InvalidInputError:
                display_message("Invalid input.")
            except BalanceToLowError:
                display_message("You do not have enough money.")
            except ItemNotInStockError:
                display_message("This item is currently not in stock.")
            except InvalidLoginError:
                display_message("Something went wrong while trying to login.")

    def handle_input(self):
        """
        Handles the users input and calls the\n
        corresponding methods

        :return: None
        """
        option = input("Input: ")

        if option == "q":
            sys.exit(0)

        elif option == "c":
            self.active_acc = create_account()

        elif option == "l":
            self.active_acc = login()

        elif option == "r":
            self._restock()

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
        if not self.snacks[index].buy():
            raise ItemNotInStockError

        self.active_acc.subtract_balance(self.snacks[index].price)
        display_message(f"Bought {self.snacks[index].name.strip()}.")

    def add_balance(self):
        """
        This method enables the user to add balance to the snack machine.

        :return: None
        """
        os.system("clear")

        added_balance = float(input("Amount: ").replace("b", "").strip())
        self.active_acc.add_balance(added_balance)

    def display(self):
        """
        Formats the object's data for TuiEngine.
        Then runs TuiEngine.render().

        :return: None
        """
        title = "Snack Machine"
        infos = {"Account": self.active_acc.get_name(),
                 "Balance": f"{self.active_acc.get_balance():.2f}€",
                 "How to use        ": "",
                 "Create acccount   ": "Enter 'c'",
                 "Login to account  ": "Enter 'l'",
                 "Add balance       ": "Enter 'b'",
                 "Buy an item       ": "Enter item id",
                 "Restock Items     ": "Enter 'r'",
                 "Exit              ": "Enter 'q'"}

        options = []
        for index, snack in enumerate(self.snacks):
            if snack.amount > 0:
                options.append(f"{index} | {snack.name} ({snack.amount}x): {snack.price:.2f}€")

        self.engine.render(title=title, data=infos, options=options)
