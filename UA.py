import csv

def print_ukrainian_airports(filename) :
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')

        for row in reader:
            if row.get('iso_country') == 'UA':
                print(row.get('name'))

print_ukrainian_airports('airport-codes_csv.csv')
