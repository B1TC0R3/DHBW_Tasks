import snack
from tui_engine import TuiEngine
from pynput import keyboard


class SnackMachine:
    balance = 0.0
    snacks = []
    engine = TuiEngine()

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
        if key is keyboard.Key.down:
            self.engine.selection_down()

        if key is keyboard.key.up:
            self.engine.selection_up()

        if key is keyboard.Key.space:
            self.engine.execute_selected_item()

    def add_balance(self):
        os.system("clear")

        added_balance = float(input("Amount: "))
        self.balance += added_balance

    def display(self):
        infos = {"Balance": f"{balance:.2f}€"}
        options = {}

        for snack in self.snacks:
