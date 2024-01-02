import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments.")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments.")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Invalid argument.")

try:
    with open(sys.argv[1]) as file:
        print(sum(1 for line in file if line.strip() and not line.lstrip().startswith("#")))

except FileNotFoundError:
    sys.exit("File does not exist.")
