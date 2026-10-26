# CS50 - Vanity Plates: checks if a license plate follows all the rules
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# A plate is valid only if it passes every rule (each rule is its own function)
def is_valid(s):
    return (
        has_valid_length(s)
        and starts_with_two_letters(s)
        and only_alphanumeric(s)
        and numbers_at_end(s)
    )

# Rule 1: between 2 and 6 characters
def has_valid_length(s):
    return 2 <= len(s) <= 6

# Rule 2: the first two characters must be letters
def starts_with_two_letters(s):
    return s[:2].isalpha()

# Rule 3: no periods, spaces or punctuation (only letters and digits)
def only_alphanumeric(s):
    return s.isalnum()

# Rule 4: numbers only at the end, and the first number cannot be 0
def numbers_at_end(s):
    for i, c in enumerate(s):
        if c.isdigit():# found the first digit
            if c == "0":
                return False
            return s[i:].isdigit() # everything from here to the end must be digits
    return True  # no digits at all is also valid


main()
