from pynput import keyboard


def on_key_press():
    pass


def placeholder():
    pass


def main():
    title = "The wonderful Snack Machine"
    info = {"Balance": "100$",
            "Products available": "Unknown"}
    options = {"Do nothing once": placeholder,
               "Do nothing again": placeholder}

    with keyboard.Listener(on_press=on_key_press()) as listener:
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
