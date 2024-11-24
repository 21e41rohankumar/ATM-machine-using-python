# ATM-machine-using-python
Tools and Libraries Used to Build the ATM Application (Explained)
Python:

The main programming language used to develop the logic and functionality of the ATM.
tkinter:

A Python library used to create the graphical user interface (GUI).
It provides tools like buttons, labels, input fields, and more to design the ATM interface.
messagebox:

A module within tkinter that displays pop-up messages such as warnings, errors, or information.
Used to show outputs like "Invalid PIN" or "Insufficient Balance."
Main Components of the ATM Application
PIN System:

A secure mechanism to log into the ATM system.
Verifies the user's input against the stored PIN before granting access.
Check Balance:

Displays the user's current account balance in a pop-up window.
Deposit Money:

Allows the user to add money to their account.
Includes a sub-window where the user enters the amount they wish to deposit.
Withdraw Money:

Enables the user to withdraw money if their balance is sufficient.
Validates that the withdrawal amount does not exceed the available balance.
Mini Statement:

Shows the last 5 transactions performed by the user, such as deposits or withdrawals.
Displays the history in a neatly formatted pop-up.
Change PIN:

Allows users to securely update their ATM PIN.
Ensures the new PIN is a 4-digit number and matches the confirmation input.
Exit Button:

Closes the application window when clicked.
Key GUI Methods and Features
pack():

A method in tkinter used to organize and arrange widgets (like buttons and labels) within the application window.
Automatically stacks elements vertically or horizontally.
Entry:

Input fields for users to enter data, such as the ATM PIN or amounts for transactions.
Includes a show="*" parameter for secure PIN entry.
Button:

Clickable buttons that trigger actions such as checking the balance, depositing money, or withdrawing money.
