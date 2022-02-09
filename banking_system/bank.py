import Xlib
import os
from pynput import keyboard

import account_manager
from tui_engine import render, \
                       execute_selection,\
                       select_next,\
                       select_prev


title = ""

info = {}
options = {}

acc = None

in_main_menu = True


def login():
    global info
    global options
    global acc

    os.system("clear")

    options = {"Transfer Money": transfer_money,
               "Log out": log_out}

    username = input("Username: ")
    pwd = input("Password: ")

    acc = account_manager.login_account(username, pwd)
    info = acc.data


def transfer_money():
    if not acc:
        return


def log_out():
    pass


def quit_bank():
    exit(0)


def load_main_manu():
    global title
    global info
    global options

    title = "FN Bank"
    info = {"Info": "Use arrow keys to navigate, select with space",
            "Account": "Currently not logged in"}

    options = {"Login": login,
               "Quit": quit_bank}


def on_press(key):
    if key == keyboard.Key.space:
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
