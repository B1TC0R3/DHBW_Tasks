import os
from exceptions import InvalidArgumentException

_acc_dir = ".accounts"


def acc_dir() -> str:
    return _acc_dir


def check_args(*args):
    for arg in args:
        if arg is None:
            raise InvalidArgumentException()


def file_exists(name: str) -> bool:
    return os.path.isfile(f"{_acc_dir}/{name}.json")