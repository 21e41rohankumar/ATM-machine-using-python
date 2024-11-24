import tkinter as tk
from tkinter import messagebox

class ATMApp:
    def __init__(self, root):
        self.pin = "1234"  # Default PIN
        self.balance = 1000  # Starting balance
        self.transaction_history = []  # To store transactions
        
        self.root = root
        self.root.title("ATM Machine")
        
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)
        
        # Label for title
        self.title_label = tk.Label(self.main_frame, text="Welcome to ATM", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)
        
        # PIN entry field
        tk.Label(self.main_frame, text="Enter PIN:", font=("Arial", 14)).pack()
        self.pin_entry = tk.Entry(self.main_frame, font=("Arial", 14), show="*")
        self.pin_entry.pack(pady=5)
        
        # Login button
        self.login_button = tk.Button(self.main_frame, text="Login", font=("Arial", 14), command=self.verify_pin)
        self.login_button.pack(pady=10)

    def verify_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.pin_entry.delete(0, tk.END)
            self.main_frame.destroy()
            self.show_menu()
        else:
            messagebox.showerror("Invalid PIN", "The PIN you entered is incorrect.")

    def show_menu(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=20)
        
        tk.Label(self.menu_frame, text="ATM Menu", font=("Arial", 18, "bold")).pack(pady=10)
        
        tk.Button(self.menu_frame, text="Check Balance", font=("Arial", 14), command=self.check_balance).pack(pady=5)
        tk.Button(self.menu_frame, text="Deposit Money", font=("Arial", 14), command=self.deposit_money).pack(pady=5)
        tk.Button(self.menu_frame, text="Withdraw Money", font=("Arial", 14), command=self.withdraw_money).pack(pady=5)
        tk.Button(self.menu_frame, text="Mini Statement", font=("Arial", 14), command=self.mini_statement).pack(pady=5)
        tk.Button(self.menu_frame, text="Change PIN", font=("Arial", 14), command=self.change_pin).pack(pady=5)
        tk.Button(self.menu_frame, text="Exit", font=("Arial", 14), command=self.root.quit).pack(pady=5)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ₹{self.balance:.2f}")
    
    def deposit_money(self):
        def deposit():
            try:
                amount = float(deposit_entry.get())
                if amount > 0:
                    self.balance += amount
                    self.transaction_history.append(f"Deposited: ₹{amount:.2f}")
                    messagebox.showinfo("Success", f"₹{amount:.2f} deposited successfully!")
                    deposit_window.destroy()
                else:
                    messagebox.showwarning("Invalid Amount", "Please enter a positive amount.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")
        
        deposit_window = tk.Toplevel(self.root)
        deposit_window.title("Deposit Money")
        tk.Label(deposit_window, text="Enter amount to deposit:", font=("Arial", 14)).pack(pady=10)
        deposit_entry = tk.Entry(deposit_window, font=("Arial", 14))
        deposit_entry.pack(pady=5)
        tk.Button(deposit_window, text="Deposit", font=("Arial", 14), command=deposit).pack(pady=10)

    def withdraw_money(self):
        def withdraw():
            try:
                amount = float(withdraw_entry.get())
                if amount <= 0:
                    messagebox.showwarning("Invalid Amount", "Please enter a positive amount.")
                elif amount > self.balance:
                    messagebox.showwarning("Insufficient Balance", "You do not have enough balance.")
                else:
                    self.balance -= amount
                    self.transaction_history.append(f"Withdrawn: ₹{amount:.2f}")
                    messagebox.showinfo("Success", f"₹{amount:.2f} withdrawn successfully!")
                    withdraw_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")
        
        withdraw_window = tk.Toplevel(self.root)
        withdraw_window.title("Withdraw Money")
        tk.Label(withdraw_window, text="Enter amount to withdraw:", font=("Arial", 14)).pack(pady=10)
        withdraw_entry = tk.Entry(withdraw_window, font=("Arial", 14))
        withdraw_entry.pack(pady=5)
        tk.Button(withdraw_window, text="Withdraw", font=("Arial", 14), command=withdraw).pack(pady=10)

    def mini_statement(self):
        if not self.transaction_history:
            messagebox.showinfo("Mini Statement", "No transactions available.")
        else:
            statement = "\n".join(self.transaction_history[-5:])  # Show last 5 transactions
            messagebox.showinfo("Mini Statement", f"Last 5 transactions:\n{statement}")

    def change_pin(self):
        def update_pin():
            new_pin = pin_entry.get()
            confirm_pin = confirm_pin_entry.get()
            if len(new_pin) != 4 or not new_pin.isdigit():
                messagebox.showerror("Error", "PIN must be a 4-digit number.")
            elif new_pin != confirm_pin:
                messagebox.showerror("Error", "PINs do not match.")
            else:
                self.pin = new_pin
                messagebox.showinfo("Success", "PIN changed successfully!")
                pin_window.destroy()
        
        pin_window = tk.Toplevel(self.root)
        pin_window.title("Change PIN")
        tk.Label(pin_window, text="Enter new PIN:", font=("Arial", 14)).pack(pady=10)
        pin_entry = tk.Entry(pin_window, font=("Arial", 14), show="*")
        pin_entry.pack(pady=5)
        tk.Label(pin_window, text="Confirm new PIN:", font=("Arial", 14)).pack(pady=10)
        confirm_pin_entry = tk.Entry(pin_window, font=("Arial", 14), show="*")
        confirm_pin_entry.pack(pady=5)
        tk.Button(pin_window, text="Change PIN", font=("Arial", 14), command=update_pin).pack(pady=10)

# Create the application window
root = tk.Tk()
app = ATMApp(root)
root.mainloop()
