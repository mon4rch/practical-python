#!/usr/bin/python3

# mortgage.py. Exercise 1.7 Dave's Mortgage

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_of_months = 0
extra_pay = 1000.0

while num_of_months !=12:
	principal = principal * (1+rate/12) - (payment + extra_pay)
	total_paid += (payment+extra_pay) 
	num_of_months+=1


while principal > 0:
	
	principal = principal * (1+rate/12) - payment
	total_paid += payment 
	num_of_months +=1
              		
print('Total paid', round(total_paid, 4), 'over a period of', num_of_months)

