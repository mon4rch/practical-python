#!/usr/bin/python3
# report.py - Exercise 2.4 A list of tuples
import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    'Computes the total cost (shares*price) of a portfolio file'
    portfolio=[]

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, line in enumerate(rows):
            record = dict(zip(headers, line))
            holding_dict = {
            'name':   record['name'], 
            'shares': int(record['shares']), 
            'price':  float(record['price'])
            }
            portfolio.append(holding_dict)
        return portfolio

def read_prices(filename):
	'This functions reades prices from Data/prices.csv file'
	print(f'Reading file {filename}...\n')
	prices = {}
	with open(filename, 'rt') as file:
		r = csv.reader(file)
		for i, line in enumerate(r, start=1):
		    if line == {}:
		    	print(f'no record at row {i}')
		    	continue
		    try:
		    	prices[line[0]]=float(line[1])
		    except (ValueError, IndexError):
		    	print(f'\nRow{i}: Couldn\'t convert: {line}\n\n')
		    	pass
		return prices

def make_report(portfolio_data, stock_prices):
	prices = read_prices(stock_prices)
	portfolio = read_portfolio(portfolio_data)
	dollar_sign = '$'
	headers = ('Name', 'Shares', 'Price', 'Change')
	#create x number of spaces between header values
	s = ' ' * 4
	print(s.join(headers))
	print(('-' * 8 + ' ') * len(headers))
	for line in portfolio:
		price_prices = float(prices[line['name']])
		price_portfolio = float(line['price'])
		#value = abs(((price_prices - price_portfolio)/price_portfolio) * 100) Gain/Loss as a percentage
		value = price_prices - price_portfolio  
		print(f'{line["name"]:<10s}{line["shares"]:<10.2f} {dollar_sign}{line["price"]:<10.2f}{value:<15.2f}')
		
	return f'\nProgram ran successfully'
	
	
	

if __name__ == '__main__':
	if len(sys.argv) > 1:
		make_report(sys.argv[1], sys.argv[2])
	else:
		print("You can run the program from the command line using this format:\npython3 report.py 'file1.csv' 'file2.csv'. Or, simply run python3 to run default files")
		print(make_report('Data/portfolio.csv', 'Data/prices.csv'))

