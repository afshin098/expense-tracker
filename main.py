from expense import Expense
from expense_manager import ExpenseManager
import os

def clear_screen():
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Linux/Mac
        os.system("clear")
        print("Terminal cleared using OS check")


def menu():
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Expense")
    print("3. Delete Expense")
    print("4. Show Total")
    print("5. Exit")


manager = ExpenseManager()

while True:
    menu()

    try:
        option = int(input("Choose an option: "))
        if option == 1:
            clear_screen()
            manager.add_expense()
        elif option == 2:
            clear_screen()
            manager.show_expense()
        elif option == 3:
            clear_screen()
            manager.delete_expense()
        elif option == 4:
            clear_screen()
            manager.show_total()
        elif option == 5:
            print("Bye!")
            break
        else:
            print("Invalid Number... Try Again")
            continue
    except ValueError:
        print("Invalid Input...Try Again")
