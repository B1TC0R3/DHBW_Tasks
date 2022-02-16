import Xlib.error
from pynput import keyboard
from tui_engine import TuiEngine
from snack_machine import SnackMachine


engine = None


def on_key_press(key):
    global engine

    if key == keyboard.Key.down:
        engine.selection_down()

    if key == keyboard.Key.up:
        engine.selection_up()

    if key == keyboard.Key.space:
        engine.execute_selected_item()


def add_balance():
    os.system("clear")
    balance = input("Enter amount: ")


def main():
    snack_machine = SnackMachine(balance=0.0)
    snack_machine.run()


if __name__ == "__main__":
    main()
else:
    print("Please run snack_machine.py as the main file.")
    exit(-1)
