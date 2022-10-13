import csv, sys

rows = []
filename = 'data.csv'
with open(filename, encoding='utf8', newline='') as file:
    reader = csv.reader(file)
    try:
        for row in reader:
            print(len(row), row[0], '\n', row)
            rows.append(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
