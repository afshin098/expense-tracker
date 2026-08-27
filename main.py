expense_list = []


class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category


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
        amount = int(input("Amount:"))
        category = input("Category:")
        expense_list.append(Expense(title, amount, category))

        q = input("Add another Expense? y/n").lower()
        if q != "y":
            break


def show_expense():
    print("===== Expense List =====")
    for id, expense in enumerate(expense_list, start=1):
        print(f"{id}. {expense.title} - {expense.amount} - {expense.category}")


def delete_expense():
    option = int(input("Select a Index to delete: ")) - 1
    selected_item = expense_list.pop(option)
    print(
        f"You Are Deleting {selected_item.title} - {selected_item.amount} - {selected_item.category}"
    )


def show_total():
    total = 0
    for expense in expense_list:
        total += expense.amount
    print(f"===== Total: {total} =====")


while True:
    menu()
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
