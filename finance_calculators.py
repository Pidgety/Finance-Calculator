"""This program contains two finance calculators: an investment calculator
that allows the user to calculate simple or compound interest and a bond
repayment calculator that calculates monthly repayment amounts."""
from tkinter import *
from tkinter import messagebox
import math
import os

# CONSTANTS #
FONT = ("Calibri", 14, "normal")
# add colour palette here

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
    result_lbl.config(text=f"The total amount after interest is £ INSERT RESULT .")
    result_lbl.grid(row=11, column=1, columnspan=2, sticky="w")


def calculate_mortgage():
    """Accesses mortgage calculation values, validates input and 
    presents the result."""
    result_lbl.config(text=f"Your monthly repayment amount is £ INSERT RESULT .")
    result_lbl.grid(row=11, column=1, columnspan=2, sticky="w")


def investment_setup():
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
    label1.config(text="Current value of the property:")
    pound_lbl.grid(row=5, column=2, sticky="e")
    entry1.grid(row=5, column=3)

    label2.grid(row=6, column=1, sticky="w")
    entry2.grid(row=6, column=3)
    percentage_lbl.grid(row=6, column=4)

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
window.config(padx=40, pady=40)

welcome_lbl = Label(text="Please select the type of calculation you wish to make:", pady=10, font=FONT)
welcome_lbl.grid(row=0, column=1, columnspan=2)

radio_state = IntVar()

investment_btn = Radiobutton(text="Investment interest", value=1,
                             variable=radio_state, font=FONT,
                             command=investment_setup)
investment_btn.grid(row=2, column=1, sticky="w")

mortgage_btn = radiobutton2 = Radiobutton(text="Mortgage repayments", value=2,
                                          variable=radio_state, font=FONT,
                                          command=mortgage_setup)
mortgage_btn.grid(row=3, column=1, sticky="w")

blank_lbl1 = Label()
blank_lbl2 = Label()
blank_lbl1.grid(row=4, column=1)
blank_lbl2.grid(row=9, column=1, pady=10)

# Label / Entry set 1
# Investment - money to deposit in £s
# Mortgage - current value of property in £s
label1 = Label(font=FONT, pady=10)
label1.grid(row=5, column=1, sticky="w")
entry1 = Entry(width=20)
pound_lbl = Label(text="£",font=FONT)

# Label / Entry set 2
# Investment & Mortgage - interest rate as a float
label2 = Label(text="Interest rate:",font=FONT)
percentage_lbl = Label(text="%", font=FONT)
entry2 = Entry(width=20)

# Label / Entry set 3
# Investment - investment period in years
# Mortgage - number of years to repay mortgage over
label3 = Label(font=FONT, pady=10)
label3.grid(row=7, column=1, sticky="w")
years_lbl = Label(text="years", font=FONT)
entry3 = Entry(width=20)

# Label / Entry set 4
# Investment type - simple or compound
label4 = Label(font=FONT)

investment_type_state = IntVar()
simple_btn = Radiobutton(text="Simple", value=1,
                             variable=investment_type_state, font=FONT)
compound_btn = Radiobutton(text="Compound", value=2,
                             variable=investment_type_state, font=FONT)

# Calculate button
calculate_btn = Button(text="Calculate", font=FONT,command=select_calculation)

# Result display label
result_lbl = Label(font=FONT, pady=20)


# print("1.   Investment - calculate the amount of interest you'll earn on "
#     "your investment.\n")
# print("2.   Mortgage - calculate the monthly repayment amounts on a home "
#         "loan.\n")


# # If user selects investment, prompt user to input details until valid.
# # Store recast values for calculations.
# if calc_type == "1":
#     clear_screen()
#     print("\n\033[1mInvestment calculator\033[0m")
#     while True:
#         investment_amount = input("\nPlease enter the amount of money you "
#                                 "wish to deposit (in £s): ")
#         if investment_amount.isnumeric():
#             investment_amount = int(investment_amount)
#             break

#     while True:
#         try:
#             interest_rate = float(input("\nPlease enter the interest rate as a "
#                                 "number (without the % symbol): "))
#         except ValueError:
#             print("\nInvalid - please enter a number.")
#             continue
#         else:
#             break

#     while True:
#         investment_years = input("\nPlease enter the investment period "
#                                 "in years: ")
#         if investment_years.isnumeric():
#             investment_years = int(investment_years)
#             break

# # Request interest type input and loop until valid.
#     print("\nWhich type of interest would you like to calculate?\n"
#         "\n1.  Simple\n"
#         "\n2.  Compound")
#     while True:
#         interest_type = input("\nPlease enter an option number: ")
#         if interest_type.isnumeric():
#             if interest_type in ("1", "2"):
#                 break

#     # If simple is selected,
#     # calculate and print simple interest on investment.
#     if interest_type == "1":
#         total_after_interest = (investment_amount
#             * (1 + ((interest_rate/100) * investment_years)))
#         print("\nThe total amount after applying simple interest is "
#             f"£{round(total_after_interest, 2)}.\n")

#     # If compound is selected,
#     # calculate and print compound interest on investment.
#     else:
#         total_after_interest = (investment_amount
#                 * math.pow((1 + (interest_rate/100)), investment_years))
#         print("\nThe total amount after applying compound interest is "
#             f"£{round(total_after_interest, 2)}.\n")

# # If Mortgage is selected, prompt for inputs until valid, recast as int/float.
# # Calculate and print monthly repayment amount.
# else:
#     clear_screen()
#     print("\n\033[1mMortgage repayments calculator\033[0m\n")
#     while True:
#         house_value = input("\nPlease enter the current value of the "
#                             "house (in £s), using numbers only: ")
#         if house_value.isnumeric():
#             house_value = int(house_value)
#             break
#     while True:
#         try:
#             interest_rate = float(input("\nPlease enter the interest rate as a "
#                                 "number (without the % symbol): "))
#         except ValueError:
#             print("Invalid - please enter a number.")
#             continue
#         else:
#             break
#     while True:
#         years_remaining = input("\nPlease enter the number of years "
#                                 "you plan to repay the mortgage over: ")
#         if years_remaining.isnumeric():
#             months_remaining = int(years_remaining) * 12
#             break
#     monthly_interest = (interest_rate/100)/12
#     monthly_repayment = (((monthly_interest * house_value)
#                         / (1 - (1+monthly_interest)
#                         ** (-months_remaining))))
#     print("\nThe monthly repayment amount is "
#             f"£{round(monthly_repayment, 2)}.\n")

window.mainloop()
