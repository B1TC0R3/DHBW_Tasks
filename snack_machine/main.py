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
    global engine

    engine = TuiEngine()
    snack_machine = SnackMachine(balance=20.0)

    title = "The wonderful Snack Machine"
    info = {"Balance": "0$",
            "Products available": "Unknown",
            "How to use": "Arrow keys to change selection, space to select"}
    options = {"Add Balance": add_balance,
               "Exit": exit}

    engine.render(title, info, options)

    try:
        with keyboard.Listener(on_key_press) as listener:
            while True:
                listener.join()
    except TypeError:
        print("There has been an error while trying to read a value!")
    except KeyboardInterrupt:
        print("Input-listener stopped.\nExiting Application.")
    except Xlib.error.ConnectionClosedError:
        print("Failed to normally stop input-listener.\nForced stop.\nExiting Application.")


if __name__ == "__main__":
    main()
else:
    print("Please run snack_machine.py as the main file.")
    exit(-1)
