#!/usr/bin/python3
# pcost.py Exercise 1.27: Reading a data file
total_cost = 0
shares=[]
print("Reading file 'Portfolio.csv'...\n")
with open('Data/portfolio.csv', 'rt') as file:
    next(file)
    for line in file:
        line = line.strip('\n')
        line = line.split(',')
        total_cost += float(line[2])

    print(f'Total cost of shares is {round(total_cost, 4)}')
    print('Closing file...\n')

