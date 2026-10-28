# Lines of Code - CS50P Problem Set 6

import sys


def main():
    filename = check_args(sys.argv)
    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(sum(1 for line in lines if is_code(line)))


def check_args(argv):
    """Validate command-line arguments and return the filename."""
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    if not argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    return argv[1]


def is_code(line):
    """Return True if the line is not blank and not a comment."""
    # strip() also catches indented comments and whitespace-only lines
    stripped = line.strip()
    return stripped != "" and not stripped.startswith("#")


if __name__ == "__main__":
    main()
