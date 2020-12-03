#!/usr/bin/python3 
#fileparse.py Exercise 3.3 

import csv

def parse_csv(filename, select=None, types = [str, int, float], has_headers=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as file:
        rows = csv.reader(file)
        #Read file headers
        if has_headers:
            headers = next(rows)
        else:
            if types and not has_headers:
                holdings = {}
                for row in rows:
                    row = [func(val) for func, val in zip(types, row)]
                    try:
                        holdings[row[0]] = row[1]
                    except (ValueError, IndexError):
                        continue
                print(holdings)
                return [(v,k) for v, k in holdings.items()]

        if select:
            indices = [headers.index[colname] for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:       #skip blank lines
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if indices:
                row = [row[index] for index in indices]
            record = dict(zip(headers, row))
            records.append(record)
            return records

