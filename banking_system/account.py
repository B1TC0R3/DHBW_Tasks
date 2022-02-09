import json
from exceptions import BalanceToLowException, \
                       RecipientNotFoundException, \
                       InvalidTransferAmountException
from utility import *


class Account:
    data = {
        "name": "",
        "pwd": "",
        "balance": 0.0,
        "transactions": []
    }

    def __init__(self, name: str, pwd: str):
        self.data["name"] = name
        self.data["pwd"] = pwd

    # add 100$ to the account
    # for demonstration purposes
    def work(self):
        self.data["balance"] += 100.0

        with open(f"{acc_dir()}/{self.data['name']}.json", "w") as acc_file:
            json.dump(self.data, acc_file)
            acc_file.close()

    def transfer(self, amount: float, recipient: str):
        check_args(amount, recipient)

        if amount < 0:
            raise InvalidTransferAmountException()
        if amount > self.data["balance"]:
            raise BalanceToLowException()
        if not file_exists(recipient):
            raise RecipientNotFoundException()

        self.data["balance"] -= amount
        self.data["transactions"].append(f"\n\t-{amount}$ to {recipient}")

        with open(f"{acc_dir()}/{recipient}.json", "r") as recipient_file:
            recipient_acc = Account(None, None)
            recipient_acc.data = json.load(recipient_file)

            recipient_acc.data["balance"] += amount
            recipient_acc.data["transactions"].append(f"\n\t+{amount}$ from {self.data['name']}")

        with open(f"{acc_dir()}/{recipient}.json", "w") as recipient_file:
            json.dump(recipient_acc.data, recipient_file)

        with open(f"{acc_dir()}/{self.data['name']}.json", "w") as acc_file:
            json.dump(self.data, acc_file)
