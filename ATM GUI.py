from tkinter import *
from tkinter import messagebox


class Account:
    def __init__(self, balance):
        self.balance = balance


class ATMUI:
    def __init__(self):
        self.balance = 100000
        self.accumulated_withdrawal = 0
        self.account = None

    def main(self):
        self.draw_welcome_ui()

    def draw_welcome_ui(self):
        self.frame = Tk()
        self.frame.title("X Bank")

        self.welcome_label = Label(self.frame, text="Welcome to BHU Bank")
        self.pin_label = Label(self.frame, text="Enter PIN:")
        self.pin_textfield = Entry(self.frame, show="*")
        self.login_btn = Button(self.frame, text="Login", command=self.draw_account_type_ui)

        self.welcome_label.grid(row=0, column=0, pady=10)
        self.pin_label.grid(row=1, column=0)
        self.pin_textfield.grid(row=1, column=1)
        self.login_btn.grid(row=2, column=0, columnspan=2, pady=10)

        self.frame.mainloop()

    def draw_account_type_ui(self):
        entered_pin = self.pin_textfield.get()
        self.pin_textfield.delete(0, 'end')

        if entered_pin != "5555":
            messagebox.showerror("Error", "Incorrect PIN. Please try again.")
            return

        self.account_type_frame = Tk()
        self.account_type_frame.title("Choose Account Type")

        self.account_type_label = Label(self.account_type_frame, text="Choose Account Type:")
        self.savings_btn = Button(self.account_type_frame, text="Savings", command=self.draw_transaction_ui)
        self.current_btn = Button(self.account_type_frame, text="Current", command=self.draw_transaction_ui)

        self.account_type_label.grid(row=0, column=0, pady=10)
        self.savings_btn.grid(row=1, column=0, pady=5)
        self.current_btn.grid(row=2, column=0, pady=5)

        self.account_type_frame.mainloop()

    def draw_transaction_ui(self):
        self.transaction_frame = Tk()
        self.transaction_frame.title("What do you want to do?")

        self.transaction_label = Label(self.transaction_frame, text="What do you want to do?")
        self.deposit_btn = Button(self.transaction_frame, text="Deposit", command=self.draw_deposit_ui)
        self.withdraw_btn = Button(self.transaction_frame, text="Withdraw", command=self.draw_withdraw_ui)

        self.transaction_label.grid(row=0, column=0, pady=10)
        self.deposit_btn.grid(row=1, column=0, pady=5)
        self.withdraw_btn.grid(row=2, column=0, pady=5)

        self.transaction_frame.mainloop()

    def draw_deposit_ui(self):
        self.deposit_frame = Tk()
        self.deposit_frame.title("Deposit")

        self.deposit_label = Label(self.deposit_frame, text="Enter deposit amount:")
        self.deposit_textfield = Entry(self.deposit_frame)
        self.deposit_amount_btn = Button(self.deposit_frame, text="Deposit", command=self.deposit)

        self.deposit_label.grid(row=0, column=0, pady=10)
        self.deposit_textfield.grid(row=1, column=0, pady=5)
        self.deposit_amount_btn.grid(row=2, column=0, pady=5)

        self.deposit_frame.mainloop()

    def deposit(self):
        try:
            amount = float(self.deposit_textfield.get())
            messagebox.showinfo("Deposit", "Deposited: " + str(amount))
            self.deposit_frame.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def draw_withdraw_ui(self):
        self.withdraw_frame = Tk()
        self.withdraw_frame.title("Withdraw")

        self.withdraw_label = Label(self.withdraw_frame, text="Enter withdrawal amount:")
        self.withdraw_textfield = Entry(self.withdraw_frame)
        self.withdraw_amount_btn = Button(self.withdraw_frame, text="Withdraw", command=self.withdraw)

        self.withdraw_label.grid(row=0, column=0, pady=10)
        self.withdraw_textfield.grid(row=1, column=0, pady=5)
        self.withdraw_amount_btn.grid(row=2, column=0, pady=5)

        self.withdraw_frame.mainloop()

    def withdraw(self):
        try:
            amount = float(self.withdraw_textfield.get())
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds.")
                self.withdraw_frame.destroy()
                return

            self.balance -= amount
            messagebox.showinfo("Withdraw", "Withdrawn: " + str(amount))
            self.withdraw_frame.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    atm_ui = ATMUI()
    atm_ui.main()
