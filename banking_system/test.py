from account_manager import create_account, login_account
from exceptions import *

# create new account
print("\nTesting account creation:")
try:
    create_account("Thomas", "qwertz")
    print("Created account 'Thomas' with password 'qwertz'")

    create_account("Franziska", "lmfao")
    print("Created account 'Franziska' with password 'lmfao'")

    # creates an empty file
    # please dont ask me why, if you figure it out just tell me
    create_account("Felix", "hahadunicht")
    print("Created account 'Felix' with password 'hahadunicht'")

    create_account("Albert", "12345")
    print("Created account 'Albert' with password '12345'")

except AccountExistsException:
    print("One or more accounts already exists.\n" +
          "Account creation has been skipped.")


# login to existing account
print("\nTesting account login (Wrong pwd):")
try:
    login_account("Thomas", "Invalid")
    print("Logged into account 'Thomas' with password 'Invalid'")

except InvalidLoginException:
    print("Logins were successfully blocked.")

print("\nTesting account login (Correct pwd):")
try:
    login_account("Thomas", "qwertz")
    print("Logged into account 'Thomas' with password 'qwertz'")

except InvalidLoginException:
    print("Failed to login with correct credentials.")

# earn money
# send money from one account to another
print("\nTesting transfer services:")
try:
    acc = login_account("Thomas", "qwertz")
    acc.work()
    print("Added 100$ to account 'Thomas'")

    acc.transfer(50.0, "Albert")
    print("Transfered 50$ to Albert")
    acc.transfer(25.57, "Franziska")
    print("Transfered 25.57$ to Franziska")

    print(f"Thomas balance: {acc.data['balance']}")
    acc = login_account("Albert", "password")
    print(f"Albert balance: {acc.data['balance']}$")

except InvalidLoginException:
    print("Failed to login to worker account.")

# Test exceptions
print("\nTesting Exceptions:")
try:
    raise InvalidLoginException()
except InvalidLoginException:
    print("Raised InvalidLoginException")

try:
    raise AccountExistsException()
except AccountExistsException:
    print("Raised AccountExistsException")

try:
    raise InvalidArgumentException()
except InvalidArgumentException:
    print("Raised InvalidArgumentException")

try:
    raise BalanceToLowException()
except BalanceToLowException:
    print("Raised BalanceToLowException")
