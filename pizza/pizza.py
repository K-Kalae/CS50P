import sys
from tabulate import tabulate
import csv

if len(sys.argv)<2:
    sys.exit("Too few command line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid file")
elif len(sys.argv)>2:
    sys.exit("Too many command line arguments")

try:
    with open(sys.argv[1]) as file:
        print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist.")
