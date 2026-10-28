# Taqueria - CS50P Problem Set 3

# Dictionary: item name -> price, for direct lookup by name
MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    total = 0.0

    # Keep asking until the user presses Ctrl-D
    while True:
        try:
            # .title() makes the input match the menu keys
            item = input("Item: ").title()
        except EOFError:
            print()
            break

        try:
            total += MENU[item]
            print(f"Total: ${total:.2f}")
        except KeyError:
            # Item not on the menu: ignore it
            pass


if __name__ == "__main__":
    main()
