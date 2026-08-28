from expense import Expense


class ExpenseManager:
    def __init__(self):
        self.expense_list = []

    def is_empty(self):
        if len(self.expense_list) == 0:
            print("No expenses found.")
            return True
        else:
            return False

    def add_expense(self):
        print("===== Add Expense =====")
        while True:
            title = input("Title:")
            try:
                amount = int(input("Amount:"))
            except ValueError:
                print("invalid input")
                continue
            category = input("Category:")
            self.expense_list.append(Expense(title, amount, category))
            print(f"Expense Added: {title} - {amount} - {category}")

            q = input("Add another Expense? y/n").lower()
            if q != "y":
                break

    def show_expense(self):
        if not self.is_empty():
            print("===== Expense List =====")
            for id, expense in enumerate(self.expense_list, start=1):
                print(f"{id}. {expense.title} - {expense.amount} - {expense.category}")

    def delete_expense(self):
        if not self.is_empty():
            try:
                print("===== Delete Expense =====")
                self.show_expense()
                option = int(input("Select a Index to delete[1000 to Exit]: ")) - 1
                if option == 999:
                    print("Back to Main Menu")
                elif option < 0 or option >= len(self.expense_list):
                    print("Invalid Number... Back to main menu")
                else:
                    selected_item = self.expense_list.pop(option)
                    print(
                        f"You Are Deleting {selected_item.title} - {selected_item.amount} - {selected_item.category}"
                    )
            except ValueError:
                print("Invalid input")

    def show_total(self):
        if not self.is_empty():
            total = 0
            for expense in self.expense_list:
                total += expense.amount
            print(f"===== Total: {total} =====")
