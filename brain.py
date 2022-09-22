from tkinter import *
import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.config(pady=10, padx=50)

        #Entry for numbers
        self.calc_entry = Entry(width=35)
        self.calc_entry.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

        #Buttons
        self.button_0 = Button(text="0", padx=30, command=lambda: self.insert_number(0))
        self.button_1 = Button(text="1", padx=30, command=lambda: self.insert_number(1))
        self.button_2 = Button(text="2", padx=30, command=lambda: self.insert_number(2))
        self.button_3 = Button(text="3", padx=30, command=lambda: self.insert_number(3))
        self.button_4 = Button(text="4", padx=30, command=lambda: self.insert_number(4))
        self.button_5 = Button(text="5", padx=30, command=lambda: self.insert_number(5))
        self.button_6 = Button(text="6", padx=30, command=lambda: self.insert_number(6))
        self.button_7 = Button(text="7", padx=30, command=lambda: self.insert_number(7))
        self.button_8 = Button(text="8", padx=30, command=lambda: self.insert_number(8))
        self.button_9 = Button(text="9", padx=30, command=lambda: self.insert_number(9))

        # Grid for number buttons
        self.button_0.grid(column=0, row=4, sticky=tk.EW)
        self.button_1.grid(column=0, row=3)
        self.button_2.grid(column=1, row=3)
        self.button_3.grid(column=2, row=3)

        self.button_4.grid(column=0, row=2)
        self.button_5.grid(column=1, row=2)
        self.button_6.grid(column=2, row=2)

        self.button_7.grid(column=0, row=1)
        self.button_8.grid(column=1, row=1)
        self.button_9.grid(column=2, row=1)

        # Operation buttons
        self.button_add = Button(text="+", padx=10, command=self.add)
        self.button_multiply = Button(text="*", padx=11, command=self.multiply)
        self.button_sub = Button(text="-", padx=11, command=self.subtract)
        self.button_divide = Button(text="/", padx=11, command=self.divide)
        self.button_clear = Button(text="Clear", command=self.clear)
        self.button_equal = Button(text="=", padx=11, command=self.equal)

        # Grid for operation buttons
        self.button_add.grid(column=4, row=1)
        self.button_multiply.grid(column=4, row=2)
        self.button_sub.grid(column=4, row=3)
        self.button_divide.grid(column=4, row=4)
        self.button_clear.grid(column=2, row=4, columnspan=2, sticky=tk.EW)
        self.button_equal.grid(column=1, row=4, sticky=tk.EW)

    def insert_number(self,number):
        self.calc_entry.insert(END, number)

    def clear(self):
        self.calc_entry.delete(0, END)

    def add(self):
        global n1
        global operator
        operator = "add"
        try:
            first_number = self.calc_entry.get()
            n1 = int(first_number)
        except ValueError:
            messagebox.showerror(message="Error")
        else:
            n1 = int(first_number)
        finally:
            self.calc_entry.delete(0, END)

    def subtract(self):
        global n1
        global operator
        operator = "subtract"
        try:
            first_number = self.calc_entry.get()
            n1 = int(first_number)
        except ValueError:
            messagebox.showerror(message="Error")
        else:
            n1 = int(first_number)
        finally:
            self.calc_entry.delete(0, END)

    def multiply(self):
        global n1
        global operator
        operator = "multiply"
        try:
            first_number = self.calc_entry.get()
            n1 = int(first_number)
        except ValueError:
            messagebox.showerror(message="Error")
        else:
            n1 = int(first_number)
        finally:
            self.calc_entry.delete(0, END)

    def divide(self):
        global n1
        global operator
        operator = "divide"
        try:
            first_number = self.calc_entry.get()
            n1 = int(first_number)
        except ValueError:
            messagebox.showerror(message="Error")
        else:
            n1 = int(first_number)
        finally:
            self.calc_entry.delete(0, END)

    def equal(self):
        global n1, n2
        n2 = self.calc_entry.get()
        if operator == "add":
            total = int(n1) + int(n2)
        elif operator == "multiply":
            total = int(n1) * int(n2)
        elif operator == "subtract":
            total = int(n1) - int(n2)
        else:
            total = int(n1) / int(n2)
        self.calc_entry.delete(0, END)
        self.calc_entry.insert(0, f"Total: {total}")

    def run(self):
        self.mainloop()