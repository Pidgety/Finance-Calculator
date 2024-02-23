"""This program contains two finance calculators: an investment calculator
that allows the user to calculate simple or compound interest and a bond
repayment calculator that calculates monthly repayment amounts."""

import math
import os


def clear_screen():
    """This function clears the console screen"""
    os.system('cls')


is_running = True
while is_running:

    # Present user with the available options and store user input.
    clear_screen()
    print("\nWelcome to this set of finance calculation tools.\n\nOptions:\n")

    print("1.   Investment - calculate the amount of interest you'll earn on "
        "your investment.\n")
    print("2.   Mortgage - calculate the monthly repayment amounts on a home "
          "loan.\n")

    # Prompt user until selection input is valid.
    while True:
        calc_type = input("Please select an option by entering the relevant "
                        "number: ")
        if calc_type.isnumeric():
            if calc_type in ("1", "2"):
                break

    # If user selects investment, prompt user to input details until valid.
    # Store recast values for calculations.
    if calc_type == "1":
        clear_screen()
        print("\n\033[1mInvestment calculator\033[0m")
        while True:
            investment_amount = input("\nPlease enter the amount of money you "
                                    "wish to deposit (in £s): ")
            if investment_amount.isnumeric():
                investment_amount = int(investment_amount)
                break

        while True:
            try:
                interest_rate = float(input("\nPlease enter the interest rate as a "
                                    "number (without the % symbol): "))
            except ValueError:
                print("\nInvalid - please enter a number.")
                continue
            else:
                break

        while True:
            investment_years = input("\nPlease enter the investment period "
                                    "in years: ")
            if investment_years.isnumeric():
                investment_years = int(investment_years)
                break

    # Request interest type input and loop until valid.
        print("\nWhich type of interest would you like to calculate?\n"
            "\n1.  Simple\n"
            "\n2.  Compound")
        while True:
            interest_type = input("\nPlease enter an option number: ")
            if interest_type.isnumeric():
                if interest_type in ("1", "2"):
                    break

        # If simple is selected,
        # calculate and print simple interest on investment.
        if interest_type == "1":
            total_after_interest = (investment_amount
                * (1 + ((interest_rate/100) * investment_years)))
            print("\nThe total amount after applying simple interest is "
                f"£{round(total_after_interest, 2)}.\n")

        # If compound is selected,
        # calculate and print compound interest on investment.
        else:
            total_after_interest = (investment_amount
                    * math.pow((1 + (interest_rate/100)), investment_years))
            print("\nThe total amount after applying compound interest is "
                f"£{round(total_after_interest, 2)}.\n")

    # If Mortgage is selected, prompt for inputs until valid, recast as int/float.
    # Calculate and print monthly repayment amount.
    else:
        clear_screen()
        print("\n\033[1mMortgage repayments calculator\033[0m\n")
        while True:
            house_value = input("\nPlease enter the current value of the "
                                "house (in £s), using numbers only: ")
            if house_value.isnumeric():
                house_value = int(house_value)
                break
        while True:
            try:
                interest_rate = float(input("\nPlease enter the interest rate as a "
                                    "number (without the % symbol): "))
            except ValueError:
                print("Invalid - please enter a number.")
                continue
            else:
                break
        while True:
            months_remaining = input("\nPlease enter the number of months "
                                    "you plan to repay the mortgage over: ")
            if months_remaining.isnumeric():
                months_remaining = int(months_remaining)
                break
        monthly_interest = (interest_rate/100)/12
        monthly_repayment = (((monthly_interest * house_value)
                            / (1 - (1+monthly_interest)
                            ** (-months_remaining))))
        print("\nThe monthly repayment amount is "
              f"£{round(monthly_repayment, 2)}.\n")

    run_again = input("Please press 'y' to run another calculation, or any "
                    "other key to quit: ")
    if run_again.lower() != "y":
        is_running = False
        print("\nThank you for using this finance calculator tool.\n")
