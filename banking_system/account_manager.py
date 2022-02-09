import json
from account import Account
from exceptions import *
from utility import *


def create_account(name: str, pwd: str):
    check_args(name, pwd)

    if not os.path.isdir(acc_dir()):
        os.mkdir(acc_dir())
    if file_exists(name):
        raise AccountExistsException()

    acc = Account(name, pwd)
    with open(f"{acc_dir()}/{name}.json", "x") as acc_file:
        json.dump(acc.data, acc_file)


def login_account(name: str, pwd: str) -> Account:
    check_args(name, pwd)

    acc = Account(name, pwd)

    try:
        with open(f"{acc_dir()}/{name}.json", "r") as acc_file:
            acc.data = json.load(acc_file)
    except FileNotFoundError:
        raise InvalidLoginException

    if not pwd == acc.data["pwd"]:
        raise InvalidLoginException
    else:
        return acc
