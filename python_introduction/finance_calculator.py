monthly_income = float(input('Enter your monthly income:'))
monthly_expenses = float(input('Enter your monthly expenses:'))

#calculating monthly savings 
monthly_savings = monthly_income - monthly_expenses

#calculating the annual savings 
interest = 0.05
savings = monthly_savings * 12 + (monthly_savings * 12 * interest)

#outputing results
print('Your monthly savings are $',monthly_savings)
print('Projected savings after one year, with interest, is: $',savings)
