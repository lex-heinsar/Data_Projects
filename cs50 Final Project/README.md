# MORTGAGE LOAN CALCULATOR
#### Video Demo:  <URL HERE>
#### Description:
This project is a **Mortgage Loan Calculator** that calculates fixed monthly payments based on a given property value, down payment, interest rate, and loan term. It also generates a detailed amortization schedule that shows how each monthly payment is split between interest and principal, as well as the remaining loan balance over time.
##### CS50P Final Project submission package
1. `project.py` the final project code file in Python
2. `test_project.py` file with accompaning tets that can be executed with `pytest`
3. `requirements.txt` a list of installed libraries
4. `mortgage_schedule.csv` a mortage schedule exported to a csv file during the video demo
5. `README.md` the current readme file
### Features:
1. Calculates monthly mortgage payments using the annuity formula.
2. Generates a full amortization schedule, showing month-by-month payments.
3. Displays a mortgage summary, including total interest paid and total loan cost.
4. Allows the user to export the schedule to a CSV file for further analysis.
5. Uses structured error handling to ensure valid user input.
6. Includes a fun exit message using the `cowsay` library.
### How to Use the Mortgage Loan Calculator
#### 1. Running the Program
To execute the script, navigate to the directory containing `project.py` and run:
```
python project.py
```
#### 2. User Input
The program will prompt the user to enter:
- Property Value (e.g., 400000 for a $400,000 home)
- Down Payment (e.g., 80000 for a $80,000 down payment)
- Annual Interest Rate (%) (e.g., 5.0 for 5.0%)
- Loan Term (Years) (e.g., 30 for a 30-year mortgage)

After entering these values, the program will calculate and display the monthly mortgage payment.
#### 3. Displaying the Amortization Schedule
The user is given the option to display the full amortization schedule. If selected, a formatted table will be shown with:
- Month number
- Monthly payment amount
- Interest portion
- Principal portion
- Remaining balance
#### 4. Exporting the Amortization Schedule to a CSV file
Users can also choose to export the schedule as a CSV file (`mortgage_schedule.csv`) for further analysis in Excel or Google Sheets.
### File Structure & Explanation
The project contains a single Python script with the following main functions:
- `get_input()` → Handles user input validation for property value, down payment, interest rate, and loan term.
- `compounding(interest_rate, period)` → Calculates the monthly interest rate and total payment periods.
- `calculate_monthly_payment(loan_amount, interest_rate, period)` → Computes the fixed monthly payment using the annuity formula.
- `generate_annuity_schedule()` → Creates a detailed month-by-month loan repayment schedule.
- `display_summary(schedule)` → Displays the loan summary, including total interest paid and total amount repaid.
- `display_schedule(schedule)` → Prints the amortization schedule in a formatted table.
- `export_to_csv(schedule)` → Saves the amortization schedule as a CSV file.
### Design Choices
The design of this project was somewhat constrained by the final project requirements, which mandated a single main function and at least three additional non-nested functions that are testable with pytest. Given more flexibility, I would have structured this project using Object-Oriented Programming (OOP) by defining a `Mortgage` class to encapsulate the loan properties and related methods. However, even without OOP, the code effectively handles the mortgage calculations and amortization schedule.

To achieve clarity and maintainability, the design follows a functional approach, where each function has a clear, single responsibility. User input is validated to ensure correct data entry, and calculations are performed using the annuity formula. The amortization schedule is generated iteratively, and structured output formatting enhances readability. Additionally, a CSV export feature provides users with a convenient way to save and analyze loan details externally.
### Conclusion
This project provides a fully functional mortgage loan calculator, handling both calculation and amortization scheduling. It ensures user-friendly interactions, error handling, and structured financial data export.
Thanks for reviewing my project!
