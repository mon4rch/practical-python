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
	prices = []
	with open(filename, 'rt') as file:
		r = csv.reader(file)
		headers = ['name', 'price']
		for i, line in enumerate(r, start=1):
		    record = dict(zip(headers, line))
		    if record == {}:
		    	print(f'no record at row {i}')
		    	continue
		    try:
		    	
		    	holding_dict = {
		    	'name':  record['name'],
		    	'price': float(record['price'])
		    	}
		    	prices.append(holding_dict)
		    except ValueError:
		    	print(f'\nRow{i}: Couldn\'t convert: {line}')
		    	pass
		return prices

def make_report(stocks, pricing):
	print(pricing, type(pricing))
	dollar_sign = '$'
	headers = ('Name', 'Shares', 'Price', 'Change')
	#create x number of spaces between header values
	s = ' ' * 6
	print(s.join(headers))
	print('-------- --------  --------  --------')
	for i, line in enumerate(stocks):
		price_prices = float(pricing[i]['price'])
		price_portfolio = float(line['price'])
		#value = abs(((price_prices - price_portfolio)/price_portfolio) * 100) Gain/Loss as a percentage
		value = price_portfolio - price_prices  
		print(f'{line["name"]:^10s}{line["shares"]:^10.2f} {dollar_sign}{line["price"]:<10.2f}{value:^10.2f}')
		
	return f'Program ran successfully'
	
	
	

if __name__ == '__main__':
	prices = read_prices('Data/prices.csv')
	portfolio = read_portfolio('Data/portfoliodate.csv')
	print(make_report(portfolio, prices))

