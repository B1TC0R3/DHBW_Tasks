from pynput import keyboard
from tui_engine import TuiEngine


engine = None


def on_key_press(key):
    global engine

    if key == keyboard.Key.down:
        engine.selection_down()

    if key == keyboard.Key.up:
        engine.selection_up()

    if key == keyboard.Key.space:
        engine.execute_selected_item()


def placeholder():
    pass


def main():
    global engine

    engine = TuiEngine()

    title = "The wonderful Snack Machine"
    info = {"Balance": "100$",
            "Products available": "Unknown",
            "How to use": "Arrow keys to change selection, space to select"}
    options = {"Do nothing once": placeholder,
               "Do nothing again": placeholder,
               "Exit": exit}

    engine.render(title, info, options)

    with keyboard.Listener(on_key_press) as listener:
        while True:
            try:
                listener.join()
            except KeyboardInterrupt:
                exit(0)


if __name__ == "__main__":
    main()
else:
    print("Please run snack_machine.py as the main file.")
    exit(-1)
