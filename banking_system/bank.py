import Xlib
from pynput import keyboard
from tui_engine import render, \
                       execute_selection,\
                       select_next,\
                       select_prev


title = ""

info = {}
options = {}


def login():
    print("Logging in")


def quit_bank():
    exit(0)


def load_main_manu():
    global title
    global info
    global options

    title = "FN Bank"
    info = {"Info": "Use arrow keys to navigate",
            "Account": "Currently not logged in"}
    options = {"Login": login,
               "Quit": quit_bank}


def on_press(key):
    if key == keyboard.Key.enter:
        execute_selection()

    if key == keyboard.Key.down:
        select_next()

    if key == keyboard.Key.up:
        select_prev()


def ui_loop():
    render(title, info, options)
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                pass
    except Xlib.error.ConnectionClosedError:
        pass


load_main_manu()


while ui_loop():
    continue
