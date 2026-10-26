# CS50 - Coke Machine: asks for coins until 50 cents are paid, then gives change
amount_due = 50 # price of a Coke in cents

# Keep asking for coins while there is still money to pay
while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]: # only accept valid coins, ignore the rest
        amount_due -= coin
        
# amount_due is now 0 or negative, so the change is its opposite
print("Change Owed:", -amount_due)
