#!/usr/bin/python3

# mortgage.py. Exercise 1.9 Dave's Mortgage

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_of_months = 0
extra_pay_start_month = int(input("Enter start month\n"))
extra_pay_end_month = int(input("Enter end month\n"))
extra_pay = float(input("Enter the extra payment\n"))
month_range = extra_pay_end_month - extra_pay_start_month

if month_range <= 0:
	print("End month and start month values are incorrect!")
	exit(1)

while num_of_months !=month_range:
	principal = principal * (1+rate/12) - (payment + extra_pay)
	total_paid += (payment+extra_pay) 
	num_of_months+=1


while principal > 0:
	
	principal = principal * (1+rate/12) - payment
	total_paid += payment 
	num_of_months +=1
              		
print('Total paid', round(total_paid, 4), 'over a period of', num_of_months)

