#prompt the user to enter financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#calculate the projected savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print results
print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")