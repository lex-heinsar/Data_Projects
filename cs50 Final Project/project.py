import cowsay
import csv
import sys

# Global Variables (used to store loan details)
loan_amount = 0
annual_interest_rate = 0
loan_period_years = 0
monthly_payment = 0


def main():
    """Main function that runs the mortgage calculator"""
    print("Welcome to the Mortgage Monthly Payment Calculator.")
    print("Please follow the instructions:")

    calculate_monthly_payment(*get_input())
    schedule = generate_annuity_schedule()

    display_summary(schedule)

    # Ask user if they want to display the amort schedule
    if input("Would you like to display the Mortgage Amortization Schedule? (Type y or n): ") == "y":
        display_schedule(schedule)

    # Ask use if they want to export the schedule as a CSV file
    if input("Would you like to generate a csv file with the Mortgage Amortisation Schedule? (Type y or n): ") == "y":
        print(export_to_csv(schedule))

    # Exit message with cowsay
    cowsay.cow("Thank you for using this calculator! See you next time!")
    sys.exit()


def get_input():
    """Collects user input for property value, down payment, interest rate, and loan term.

    :return: a tuple with loan_amount, annual_interest_rate, loan_period_years
    :rtype: tuple
    """

    # Get property value (must be positive)
    while True:
        try:
            property_value = float(input("Enter the property value ($): "))
            if property_value > 0:
                break
            else:
                print("Invalid input! Please try again.")
        except:
            print("Invalid input! Please try again.")
            pass

    # Get downpayment amount (must be non-negative)
    while True:
        try:
            down_payment_amount = float(
                input("Enter the down payment amount ($): "))
            if 0 <= down_payment_amount < property_value:
                break
            else:
                print("Invalid input! Please try again.")
        except:
            print("Invalid input! Please try again.")
            pass

    # Get annual interest rate (= stated interest rate) -> percentage, converted to decimal
    while True:
        try:
            global annual_interest_rate
            annual_interest_rate = float(
                input("Enter the annual interest rate (%): ")) / 100
            if 0 < annual_interest_rate <= 1:
                break
            else:
                print("Invalid input! Please try again.")
        except:
            print("Invalid input! Please try again.")
            pass

    # get the loan period in years (must be positive)
    while True:
        try:
            global loan_period_years
            loan_period_years = int(input("Enter the loan term (years): "))
            if loan_period_years > 0:
                break
            else:
                print("Invalid input! Please try again.")
        except:
            print("Invalid input! Please try again.")
            pass

    # Calculate loan amount (Property Price - Downpayment)
    global loan_amount
    loan_amount = property_value - down_payment_amount

    return (loan_amount, annual_interest_rate, loan_period_years)


def compounding(interest_rate, period):
    """Calculates periodic interest rate and total number of periods.

    :param interest_rate (float): Annual interest rate (decimal form).
    :param period (int): Loan term in years.
    :return: a tuple with periodic_rate, total_periods
    :rtype: tuple
    """
    # the loan is paid back monthly, so 12 times in one period (= 1 year) -> it's a constant
    COMPOUNDING_FREQUENCY = 12
    # the periodic rate = annual rate divided by the compounding frequency
    periodic_rate = interest_rate / COMPOUNDING_FREQUENCY
    # total number of periods = years * compounding frequency
    total_periods = period * COMPOUNDING_FREQUENCY
    return periodic_rate, total_periods


def calculate_monthly_payment(loan_amount, interest_rate, period):
    """Calculates fixed monthly mortgage payment using annuity formula.
    :param: loan_amount (float): Total loan amount.
    :param: interest_rate (float): Annual interest rate (decimal form).
    :param: period (int): Loan term in years.
    :param: float: Monthly payment amount.
    """
    periodic_rate, total_periods = compounding(interest_rate, period)

    # Apply annuity formula to compute the monthly payment
    global monthly_payment
    monthly_payment = round(loan_amount *
                            (periodic_rate * (1 + periodic_rate) ** total_periods) /
                            ((1 + periodic_rate) ** total_periods - 1), 2)
    return monthly_payment


def generate_annuity_schedule():
    """Generates the mortgage amortization schedule.

    interest payment = remaining loan balance * periodic interest rate
    principal payment = total monthly payment - interest payment
    new loan balance = previous balance - principal payment

    :return: Amortization schedule containing dictionaries for each month.
    :rtype: list
    """

    # create an empty list
    schedule = []
    periodic_rate, total_periods = compounding(
        annual_interest_rate, loan_period_years)

    loan_remaining_amount = loan_amount

    for i in range(total_periods):
        transaction = {}
        transaction["Month"] = i + 1
        interest_amount = round(loan_remaining_amount * periodic_rate, 2)
        transaction["Monthly Payment"] = monthly_payment
        transaction["Interest"] = interest_amount
        principal_payment_amount = monthly_payment - interest_amount
        transaction["Principal"] = round(principal_payment_amount, 2)
        loan_remaining_amount -= principal_payment_amount
        transaction["Remaining Amount"] = round(loan_remaining_amount, 2)
        schedule.append(transaction)

    return schedule


def display_summary(schedule):
    """
    Displays a summary of the mortgage, including total interest paid and total amount paid.
    """
    # calculate total interest paid and total amount paid
    total_interest_paid = sum(row['Interest'] for row in schedule)
    # the loan is paid back monthly, so 12 times in one period (= 1 year) -> it's a constant
    COMPOUNDING_FREQUENCY = 12
    total_amount_paid = monthly_payment * \
        (loan_period_years * COMPOUNDING_FREQUENCY)

    # print a separator (line)
    print("-" * 75)
    print(f"LOAN TERMS:")
    print("-" * 11)
    print(f"Initial Loan Amount: ${loan_amount:,.2f}")
    print(f"Annual Interest Rate: {(annual_interest_rate * 100):.4f}%")
    print(f"Loan period: {loan_period_years} years")
    print(f"Fixed Monthly Payment: ${monthly_payment:,.2f}")
    print(f"Total Interest to be Paid: ${total_interest_paid:,.2f}")
    print(
        f"Total Amount to be Paid (Principal + Interest): ${total_amount_paid:,.2f}")
    # print a separator (line)
    print("-" * 75)


def display_schedule(schedule):
    """
    Displays the amortization schedule in a formatted table.
    """
    # print the headers first. ^ -> center alignmentl, > right alignment, < left alignment
    print(f"{'Month':>6} {'Monhtly Payment':>19} {'Interest':>13} {'Principal':>13} {'Remaining Amount':>20}")

    for row in schedule:
        print(
            f"{row['Month']:>6} {row['Monthly Payment']:>19,.2f} {row['Interest']:>13,.2f} {row['Principal']:>13,.2f} {row['Remaining Amount']:>20,.2f}")


def export_to_csv(schedule):
    """
    Exports the amortization schedule to a CSV file.
    :param: schedule (list): Amortization schedule data.
    :return: a confirmation message with file name.
    :rtype: str
    """

    file_name = 'mortgage_schedule.csv'
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
                                "Month", "Monthly Payment", "Interest", "Principal", "Remaining Amount"])
        writer.writeheader()
        writer.writerows(schedule)

    return f"Mortgage repayment schedule saves as '{file_name}'"


if __name__ == "__main__":
    main()
