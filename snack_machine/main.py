from snack_machine import SnackMachine


def main():
    snack_machine = SnackMachine(balance=0.0)
    snack_machine.run()


if __name__ == "__main__":
    main()
else:
    print("Please run snack_machine.py as the main file.")
    exit(-1)
