import tkinter as tkr
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, head):
        self.head = head
        self.head.title("CALCULATOR")

        # creating a label widget and an entry widget for entering the first number in the GUI calculator
        self.num1_label = tkr.Label(head, text="Enter first number:")
        self.num1_label.grid(row=0, column=0, padx=20, pady=20)
        self.num1_entry = tkr.Entry(head, width=50)
        self.num1_entry.grid(row=0, column=1, padx=20, pady=20)

        # creating a label widget and an entry widget for entering the first number in the GUI calculator
        self.num2_label = tkr.Label(head, text="Enter second number:")
        self.num2_label.grid(row=1, column=0, padx=20, pady=20)
        self.num2_entry = tkr.Entry(head, width=50)
        self.num2_entry.grid(row=1, column=1, padx=20, pady=20)


        # creating a label widget and an option menu for selecting the operations
        self.operation_label = tkr.Label(head, text="Choose an operation from the drop-down:")
        self.operation_label.grid(row=2, column=0, padx=20, pady=20)
        self.operation_var = tkr.StringVar(head)
        self.operation_var.set("+")  # Default operation is addition
        self.operation_menu = tkr.OptionMenu(head, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.grid(row=2, column=1, padx=20, pady=20)


        # creating a button widget for triggering the calculation process in the calculator GUI
        self.calculate_button = tkr.Button(head, text="CALCULATE", command=self.calculate)
        self.calculate_button.grid(row=3, columnspan=2, padx=20, pady=20)


        # creating a label widget and an entry widget for displaying the result of the calculation in the calculator GUI
        self.result_label = tkr.Label(head, text="RESULT:")
        self.result_label.grid(row=4, column=0, padx=20, pady=20)
        self.result_var = tkr.StringVar(head)
        self.result_entry = tkr.Entry(head, textvariable=self.result_var, state='readonly', width=20)
        self.result_entry.grid(row=4, column=1, padx=20, pady=20)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    messagebox.showerror("Error!!!", "Division by zero is not allowed")
                    return
                else:
                    result = num1 / num2

            self.result_var.set(result)
        except ValueError:
            messagebox.showerror("Error!!!", "Please enter valid numbers!")


if __name__ == "__main__":
    head = tkr.Tk()
    app = CalculatorApp(head)
    head.mainloop()
