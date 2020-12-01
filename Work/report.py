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
	with open(filename) as file:
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

if __name__ == '__main__':
	prices = read_prices('Data/prices.csv')
	portfolio = read_portfolio('Data/portfolio.csv')
	for line in portfolio:
		print(line)
		price_big = float(prices[line['name']]) 
		price_small = line['price']
		gain = ((price_big - price_small)/price_small) * 100
		if gain < 0:
			print(f'Loss is {abs(round(gain, 3))}%..\n')
		else:
			print(f'Gain is {round(gain,3)}%..\n')
	
		
		
	
	
