#file obkects
"""""
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
    f_contents = f.readline()
    print(f_contents)
"""
import csv
with open("test.csv", "r") as handler:
    reader = csv.DictReader(handler, delimiter=',')
    report = {}
    for row in reader:
        print(row)
        report = report | row
print(report)
