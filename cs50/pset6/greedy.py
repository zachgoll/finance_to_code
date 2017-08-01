import cs50



while True:
    print("How much did you give me?: ", end="")
    paid = cs50.get_float()
    if paid <= 0:
        print("You can't pay me negative money.  Have some respect!")
    if paid > 0:
        break
    
# Convert the given amount to cents

cents = round(paid*100)

# Find number of quarters and remainder

quarters = cents // 25
remainder = cents % 25

# Find the number of dimes and remainder

dimes = remainder // 10
remainder = remainder % 10 

# Find the number of nickels and remainder

nickels = remainder // 5
remainder = remainder % 5

# Find the number of pennies

pennies = remainder // 1

# Calculate total number of coins paid and print out
coins_paid = quarters + dimes + nickels + pennies
print(coins_paid)




    