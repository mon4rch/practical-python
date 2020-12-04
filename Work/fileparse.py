#!/usr/bin/python3 
#fileparse.py Exercise 3.3 

import csv

def parse_csv(filename, select=None, delimiter = ',', types = None, has_headers=True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as file:
        rows = csv.reader(file, delimiter = delimiter)
        if select and not has_headers:
            raise RuntimeError('Select is only possible with headers')
        #Read file headers
        if select and has_headers:
            headers = next(rows)
            print(headers)
            indices = [headers.index(colname) for colname in select]
            headers = select
            print(indices)
        else:
            headers = []
            indices = []
            
        records = []
        for i, row in enumerate(rows, start=1):
            if not row:       #skip blank lines
                continue
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(f'Row{i}: Couldnt convert {row}\nReason:', e)
            if indices:
                row = [row[index] for index in indices]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        return records

