"""
Module containing some functions
to easily create and log in to accounts.
"""
import json
import os
from account import Account
from exceptions import InvalidLoginError

def create_account() -> Account:
    """
    Creates a new object of type account.

    :returns: Account
    """
    os.system("clear")
    acc_name = input("Enter account name:")
    acc_pwd = input("Enter account pwd:")

    acc = Account(acc_name, acc_pwd)
    save_account(acc)
    return acc


def login() -> Account:
    """
    Logs into an existing account.

    :param name: The name of the account.
    :param pwd: The password of the account.
    :returns: Account
    """
    os.system("clear")
    acc_name = input("Username:")
    acc_pwd = input("Password:")

    if not os.path.isfile(f"{_file_dir()}/{acc_name}.json"):
        raise InvalidLoginError

    with open(f"{_file_dir()}/{acc_name}.json", "r", encoding="utf-8") as file:
        acc_dict = json.load(file)

    if not acc_pwd == acc_dict["pwd"]:
        raise InvalidLoginError

    acc = Account(acc_dict["name"], acc_dict["pwd"])
    acc.add_balance(float(acc_dict["balance"]))
    return acc

def save_account(acc: Account):
    """
    Saves an account to a json file.
    The directory is: "./.accounts/"

    :param acc: The account that will be saved.
    :returns: None
    """
    json_dict = acc.to_json()

    access = "w" if os.path.isfile(f"{_file_dir()}/{acc.get_name()}.json") else "x"
    with open(f"{_file_dir()}/{acc.get_name()}.json", access, encoding="utf-8") as file:
        json.dump(json_dict, file)


def _file_dir() -> str:
    """
    The directory the account files ought to be stored in.

    :returns: str
    """
    return "./.accounts"
