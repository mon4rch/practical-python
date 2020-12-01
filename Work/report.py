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
        for row in rows:
            holding_dict = {
            'name':   row[0], 
            'shares': int(row[1]), 
            'price':  float(row[2])
            }
            portfolio.append(holding_dict)
        return portfolio

def read_prices(filename):
	'This functions reades prices from Data/prices.csv file'
	print(f'Reading file {filename}...\n')
	prices = []
	with open(filename, 'rt') as file:
		r = csv.reader(file)
		for line in r:
			if line == [] or line == "":
				print('A blank line has been encounterd')
				pass
			else:
				holding_dict = {
				line[0]: line[0],
				line[1]: float(line[1]) 
				}
				prices.append(holding_dict)
		return dict(prices)
		
def make_report(stocks, pricing):
	dollar_sign = '$'
	headers = ('Name', 'Shares', 'Price', 'Change')
	#create x number of spaces between header values
	s = ' ' * 6
	print(s.join(headers))
	print('-------- --------  --------  --------')
	for line in stocks:
		price_prices = float(pricing[line['name']]) 
		price_portfolio = line['price']
		#value = abs(((price_prices - price_portfolio)/price_portfolio) * 100) Gain/Loss as a percentage
		value = price_prices - price_portfolio
		print(f'{line["name"]:^10s}{line["shares"]:^10.2f} {dollar_sign}{line["price"]:<10.2f}{value:^10.2f}')
	exit(0)
	
	
	

if __name__ == '__main__':
	prices = read_prices('Data/prices.csv')
	portfolio = read_portfolio('Data/portfolio.csv')
	print(make_report(portfolio, prices))
	
		
		
	
	
