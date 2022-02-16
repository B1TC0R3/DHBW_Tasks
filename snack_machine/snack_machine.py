from snack import Snack
from tui_engine import TuiEngine
from pynput import keyboard


class SnackMachine:
    balance = 0.0
    selected_item = 0
    snacks = []
    engine = TuiEngine()

    def __init__(self, balance: float):
        if not isinstance(balance, float):
            raise TypeError("'SnackMachine.balance' was not 'float'")

        self.balance = balance
        self._generate_snacks()

    def _generate_snacks(self):
        """
        Creates a list of snacks.

        :return: None
        """
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
        try:
            with keyboard.Listener(on_press=self.on_press) as listener:
                while True:
                    listener.join()
        except TypeError:
            print("There has been an error while trying to read a value!")
        except KeyboardInterrupt:
            print("Input-listener stopped.\nExiting Application.")
        except Xlib.error.ConnectionClosedError:
            print("Failed to normally stop input-listener.\nForced stop.\nExiting Application.")

    def on_press(self, key):
        """
        Manages the users keyboard inputs.

        :param key: The keycode for the pressed key
        :return: None
        """
        if key is keyboard.Key.down:
            if self.selected_item > 0:
                self.selected_item -= 1

        if key is keyboard.key.up:
            if self.selected_item < len(self.snacks)-1:
                self.selected_item += 1

        if key is keyboard.Key.space:
            self.buy_selected_snack()

    def add_balance(self):
        """
        This method enables the user to add balance to the snack machine.

        :return: None
        """
        os.system("clear")

        added_balance = float(input("Amount: "))
        self.balance += added_balance

    def buy_selected_snack(self):
        pass

    def display(self):
        """
        Formats the object's data for TuiEngine.
        Then runs TuiEngine.render().

        :return: None
        """
        infos = {"Balance": f"{balance:.2f}€"}
        options = []

        for snack in self.snacks:
            options.append(f"{snack.name} ({snack.amount}x): {snack.price:.2f}€")
