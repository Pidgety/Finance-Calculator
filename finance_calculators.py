"""This program contains two finance calculators: an investment calculator
that allows the user to calculate simple or compound interest and a bond
repayment calculator that calculates monthly repayment amounts."""
from tkinter import *
from tkinter import messagebox
import math

# CONSTANTS #
FONT = ("Calibri", 14, "normal")
CREAM = "#F8F6E3"
TEAL = "#97E7E1"
TURQUOISE = "#6AD4DD"
BLUE = "#7AA2E3"


# FUNCTIONS #

def select_calculation():
    """Accesses main radio button selection and calls the relevant
    calculation function."""
    if radio_state.get() == 1:
        calculate_interest()
    else:
        calculate_mortgage()


def calculate_interest():
    """Accesses investment calculation values, validates input and
    presents the result."""

    investment_amount = entry1.get()
    interest_rate = entry2.get()
    investment_years = entry3.get()
    interest_type = investment_type_state.get()

    try:
        investment_amount = float(investment_amount)
    except ValueError:
        messagebox.showerror(title="Error",
                            message="The investment amount must be a number.")
        return
    try:
        interest_rate = float(interest_rate)
    except ValueError:
        messagebox.showerror(title="Error",
                            message="The interest rate must be a number.")
        return
    try:
        investment_years = float(investment_years)
    except ValueError:
        messagebox.showerror(title="Error",
                            message="The investment years must be a number.")
        return

    if investment_amount <= 0 or interest_rate <=0 or investment_years <=0:
        messagebox.showerror(title="Error",
                            message="Values must be higher than zero.")
        return

    if interest_type == 1:

        # Simple interest calculation
        total_after_interest = round((investment_amount
            * (1 + ((interest_rate/100) * investment_years))), 2)
        result_lbl.config(text="The total amount after applying simple "
                          f"interest is £{total_after_interest}.")
    else:

        # Compound interest calculation
        total_after_interest = round((investment_amount
                * math.pow((1 + (interest_rate/100)), investment_years)), 2)
        result_lbl.config(text="The total amount after applying compound "
                          f"interest is £{total_after_interest}.")
    result_lbl.grid(row=11, column=1, columnspan=3, sticky="w")


def calculate_mortgage():
    """Accesses mortgage calculation values, validates input and 
    presents the result."""

    property_value = entry1.get()
    interest_rate = entry2.get()
    years_remaining = entry3.get()

    try:
        property_value = float(property_value)
    except ValueError:
        messagebox.showerror(title="Error",
                            message="The mortgage amount must be a number.")
        return
    try:
        interest_rate = float(interest_rate)
    except ValueError:
        messagebox.showerror(title="Error",
                            message="The interest rate must be a number.")
        return
    try:
        years_remaining = float(years_remaining)
    except ValueError:
        messagebox.showerror(title="Error",
                            message="The mortgage term must be a number.")
        return

    if property_value <= 0 or interest_rate <=0 or years_remaining <= 0:
        messagebox.showerror(title="Error",
                            message="Values must be higher than zero.")
        return

    # monthly repayment calculation
    months_remaining = years_remaining * 12
    monthly_interest = (interest_rate/100)/12
    monthly_repayment = round((((monthly_interest * property_value)
                        / (1 - (1+monthly_interest)
                        ** (-months_remaining)))),2)

    result_lbl.config(text="Your monthly repayment amount is "
                      f"£{monthly_repayment}.")
    result_lbl.grid(row=11, column=1, columnspan=3, sticky="w")


def clear_values():
    """Clears values from entry boxes when calculation type is changed."""
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry1.focus()


def investment_setup():
    """Set up the display to accept entries for the 
    investment calculation."""

    clear_values()

    label1.config(text="Money to deposit:")
    pound_lbl.grid(row=5, column=2, sticky="e")
    entry1.grid(row=5, column=3)

    label2.grid(row=6, column=1, sticky="w")
    entry2.grid(row=6, column=3)
    percentage_lbl.grid(row=6, column=4, sticky="w")

    label3.config(text="Investment period:")
    entry3.grid(row=7, column=3)
    years_lbl.grid(row=7, column=4, sticky="w")

    label4.config(text="Interest type:")
    label4.grid(row=8, column=1, sticky="w")
    simple_btn.grid(row=8, column=2, sticky="w")
    compound_btn.grid(row=8, column=3, sticky="w")

    calculate_btn.grid(row=10, column=2, sticky="w")

    result_lbl.config(text="")


def mortgage_setup():
    """Set up the display to accept entries for the mortgage
    calculation."""
    clear_values()

    label1.config(text="Mortgage amount remaining:")
    pound_lbl.grid(row=5, column=2, sticky="e")
    entry1.grid(row=5, column=3)

    label2.grid(row=6, column=1, sticky="w")
    entry2.grid(row=6, column=3)
    percentage_lbl.grid(row=6, column=4, sticky="w")

    label3.config(text="Mortgage term:")
    entry3.grid(row=7, column=3)
    years_lbl.grid(row=7, column=4)

    label4.config(text="")
    simple_btn.grid_forget()
    compound_btn.grid_forget()

    calculate_btn.grid(row=10, column=2, sticky="w")

    result_lbl.config(text="")


window = Tk()
window.title("Finance Calculators")
window.minsize(width=700, height=500)
window.config(padx=40, pady=40, bg=CREAM)

welcome_lbl = Label(text="Please select the type of calculation you "
                    "wish to make:", pady=10, font=FONT, bg=CREAM)
welcome_lbl.grid(row=0, column=1, columnspan=2)

radio_state = IntVar()

investment_btn = Radiobutton(text="Investment interest", value=1,
                            variable=radio_state, font=FONT, bg=CREAM,
                            selectcolor=TEAL,
                            activebackground=CREAM,
                            command=investment_setup)
investment_btn.grid(row=2, column=1, sticky="w")

mortgage_btn = radiobutton2 = Radiobutton(text="Monthly mortgage repayments",
                                        value=2, variable=radio_state,
                                        font=FONT, bg=CREAM,
                                        selectcolor=TEAL,
                                        activebackground=CREAM,
                                        command=mortgage_setup)
mortgage_btn.grid(row=3, column=1, sticky="w")

blank_lbl1 = Label(bg=CREAM)
blank_lbl2 = Label(bg=CREAM)
blank_lbl1.grid(row=4, column=1)
blank_lbl2.grid(row=9, column=1, pady=10)

# Label / Entry set 1
# Investment - money to deposit in £s
# Mortgage - current value of property in £s
label1 = Label(font=FONT, pady=10, bg=CREAM)
label1.grid(row=5, column=1, sticky="w")
entry1 = Entry(width=20, bg=TEAL)
pound_lbl = Label(text="£",font=FONT, bg=CREAM)

# Label / Entry set 2
# Investment & Mortgage - interest rate as a float
label2 = Label(text="Interest rate:",font=FONT, bg=CREAM)
percentage_lbl = Label(text="%", font=FONT, bg=CREAM)
entry2 = Entry(width=20, bg=TEAL)

# Label / Entry set 3
# Investment - investment period in years
# Mortgage - number of years to repay mortgage over
label3 = Label(font=FONT, pady=10, bg=CREAM)
label3.grid(row=7, column=1, sticky="w")
years_lbl = Label(text="years", font=FONT, bg=CREAM)
entry3 = Entry(width=20, bg=TEAL)

# Label / Entry set 4
# Investment type - simple or compound
label4 = Label(font=FONT,bg=CREAM)

investment_type_state = IntVar()
simple_btn = Radiobutton(text="Simple", value=1,
                             variable=investment_type_state,
                             font=FONT, bg=CREAM,
                             selectcolor=TEAL,
                             activebackground=CREAM)
compound_btn = Radiobutton(text="Compound", value=2,
                             variable=investment_type_state,
                             font=FONT, bg=CREAM,
                             selectcolor=TEAL,
                             activebackground=CREAM)

# Calculate button
calculate_btn = Button(text="Calculate", font=FONT,command=select_calculation,
                        bg=TURQUOISE)

# Result display label
result_lbl = Label(font=FONT, pady=20, bg=CREAM)

window.mainloop()
