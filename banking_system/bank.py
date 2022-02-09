import Xlib
import os
from pynput import keyboard
from account import Account
from account_manager import *
from exceptions import InvalidLoginException
from tui_engine import render, \
                       execute_selection,\
                       select_next,\
                       select_prev


title = ""

info = {}
options = {}

acc = None

in_main_menu = True


def get_input(message: str) -> str:
    return input(message).replace("\x1b[A", "")\
                         .replace("\x1b[B", "")\
                         .strip()


def login():
    global info
    global options
    global acc

    os.system("clear")

    username = get_input("Username: ")
    pwd = get_input("Password: ")

    try:
        acc = login_account(username, pwd)
    except InvalidLoginException:
        log_out()
        return

    load_account()

    render(title, info, options)


def transfer_money():
    global info

    if not acc:
        return

    os.system("clear")

    recipient = get_input("Recipient: ")
    amount = get_input("Amount: ")

    try:
        acc.transfer(float(amount), recipient)
    except ValueError: 
        pass

    info = acc.data
    render(title, info, options)


def work():
    global acc
    global info

    acc.work()

    info = acc.data
    render(title, info, options)


def log_out():
    global acc
    global title
    global info
    global options

    acc = None
    load_main_manu()
    render(title, info, options)


def quit_bank():
    exit(0)


def load_account():
    global options
    global info
    global acc

    options = {"Transfer Money": transfer_money,
               "Work": work,
               "Log out": log_out}
    info = acc.data


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
