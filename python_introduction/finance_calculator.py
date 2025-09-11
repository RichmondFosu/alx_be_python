# Personal Finance Calculator

#Ask for financial details
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings is: ${monthly_savings}.")

#Projected annual savings
interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print (f"Your projected annual savings is: ${projected_savings}")