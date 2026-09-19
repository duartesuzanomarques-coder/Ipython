def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        has_valid_length(s)
        and starts_with_two_letters(s)
        and only_alphanumeric(s)
        and numbers_at_end(s)
    )


def has_valid_length(s):
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    return s[:2].isalpha()


def only_alphanumeric(s):
    return s.isalnum()


def numbers_at_end(s):
    for i, c in enumerate(s):
        if c.isdigit():
            if c == "0":
                return False
            return s[i:].isdigit()
    return True


main()
