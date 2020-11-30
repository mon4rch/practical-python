#!/usr/bin/python3
# pcost.py Exercise 1.30-31: create a function for reading the portfolio files + error handling


def portfolio_cost(filename):
    'Calculates the total cost of shares in portfolio csv file'
    total_cost = 0
    print("Reading file 'Portfolio.csv'...\n")
    with open(filename, 'rt') as file:
        next(file)
        for line in file:
            line = line.strip('\n')
            line = line.split(',')
            try:
                total_cost += float(line[2])
            except (ValueError, TypeError, RuntimeError) as e:
                print(e, 'Check your file for bad lines!\n')
                pass
        return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost of shares is {round(cost, 4)}')


