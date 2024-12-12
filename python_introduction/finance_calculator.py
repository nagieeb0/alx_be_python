#User Input for Financial Details:
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

#Calculate Monthly Savings
Monthly_Savings = monthly_income - monthly_expenses

#Project Annual Savings
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

print(f"Your monthly savings are:{Monthly_Savings}$ \nProjected savings after one year, with interest, is:{Projected_Savings}$")