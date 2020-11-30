#!/usr/bin/python3
# pcost.py Exercise 1.30-31-32-33: create a function for reading the portfolio files + error handling use 'CSV# module, add command line functionality (let user pass filename from cmd/bash/terminal)
import csv
import sys

def portfolio_cost(filename):
    'Calculates the total cost of shares in portfolio csv file'
    total_cost = 0
    print("Reading file 'Portfolio.csv'...\n")
    with open(filename) as file:
        r = csv.reader(file)
        next(r)
        for line in r:
            try:
                num_shares = int(line[1])
                stock_price = float(line[2])
                total_cost += (num_shares*stock_price)
            except (ValueError, TypeError, RuntimeError) as e:
                print(e, 'Check your file for bad lines!\n')
                pass
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total cost of shares is {round(cost, 4)}$')


