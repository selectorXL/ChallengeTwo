# coding: utf-8
# Libraries 
import csv
from pathlib import Path

'''I) Automate Calculations'''

# List of loans cost 
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
total_number_of_loans = len(loan_costs)
print(f'This is the total number of loans: {total_number_of_loans}')

# What is the total of all loans?
total_value_of_loan = sum(loan_costs)
print(f'Total value of the loans: ${total_value_of_loan}')

# What is the average loan amount from the list?
average_loan_price = total_value_of_loan / total_number_of_loans
print(f'This is the average of the loans price: ${average_loan_price}')

"""II) LOAN ANALYSIS"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!
future_value = loan.get("future_value")
print(f'This is the future value: {future_value}')

remaining_months = loan.get("remaining_months")
print(f'This is the remining month: {remaining_months}')


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
discount_Rate = 0.2
# YOUR CODE HERE!
present_value = (future_value) / (1+ discount_Rate/12)** remaining_months
print(f'This is the present value: ${round(present_value, 2)}')

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!
if present_value >= future_value:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The present value of the loan is less than the loan cost.")
    print("The loan is too expensive and not worth the price.")


"""III) Perform Calculations"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# New function that will be used to calculate present value.

def present_value(future_value, remaining_months, annual_discount_rate):
    present_value = (future_value) / (1+ annual_discount_rate/12)** remaining_months
    return present_value


# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
present_value = present_value(
    future_value = 1000, 
    remaining_months = 12, 
    annual_discount_rate = 0.2
)
print(f"The present value of the loan is: ${round(present_value, 2)}")


"""IV) Filter list of loans"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []
# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)
# Print the `inexpensive_loans` list
print(f'This is the inexpensive list: {inexpensive_loans}')

"""V) Save Results"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())



print('Visualizing the data')
csv_data = Path("inexpensive_loans.csv")
with open(csv_data) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)




