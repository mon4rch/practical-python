#!/usr/bin/python3
# pcost.py Exercise 1.30-31-32-33: create a function for reading the portfolio files + error handling use 'CSV# module, add command line functionality (let user pass filename from cmd/bash/terminal)
import csv
import sys

def portfolio_cost(filename):
    'Calculates the total cost of shares in portfolio csv file'
    total_cost = 0
    print(f"Reading file {filename}...\n")
    with open(filename) as file:
        r = csv.reader(file)
        headers = next(r)
        for i, line in enumerate(r, start=1):
        	record = dict(zip(headers, line))
        	print(record)
        	try:
        	    num_shares = int(record['shares'])
        	    stock_price = float(record['price'])
        	    total_cost += (num_shares*stock_price)
        	except ValueError:
        		print(f'\nRow {i}: Couldn\'t convert {line}')
        return total_cost

				
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'
    
cost = portfolio_cost(filename)
print(f'Total cost of shares is {cost:0.2f}$')


