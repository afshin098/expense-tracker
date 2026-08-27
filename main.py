expense_list = []


class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category


def is_empty():
    if len(expense_list) == 0:
        print("No expenses found.")
        return True
    else:
        return False


def menu():
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Expense")
    print("3. Delete Expense")
    print("4. Show Total")
    print("5. Exit")


def add_expense():
    while True:
        title = input("Title:")
        try:
            amount = int(input("Amount:"))
        except ValueError:
            print("invalid input")
            continue
        category = input("Category:")
        expense_list.append(Expense(title, amount, category))

        q = input("Add another Expense? y/n").lower()
        if q != "y":
            break


def show_expense():
    if not is_empty():
        print("===== Expense List =====")
        for id, expense in enumerate(expense_list, start=1):
            print(f"{id}. {expense.title} - {expense.amount} - {expense.category}")


def delete_expense():
    if not is_empty():
        try:
            option = int(input("Select a Index to delete: ")) - 1
            if option < 0 or option >= len(expense_list):
                print("Invalid Number... Back to main menu")
            else:
                selected_item = expense_list.pop(option)
                print(
                    f"You Are Deleting {selected_item.title} - {selected_item.amount} - {selected_item.category}"
                )
        except ValueError:
            print("Invalid input")


def show_total():
    if not is_empty():
        total = 0
        for expense in expense_list:
            total += expense.amount
        print(f"===== Total: {total} =====")


while True:
    menu()

    try:
        option = int(input("Choose an option: "))
        if option == 1:
            add_expense()
        elif option == 2:
            show_expense()
        elif option == 3:
            show_expense()
            delete_expense()
        elif option == 4:
            show_total()
        elif option == 5:
            print("Bye!")
            break
        else:
            print("Invalid Number... Try Again")
            continue
    except ValueError:
        print("Invalid Input...Try Again")
