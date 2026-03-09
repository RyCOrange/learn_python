# This program calculates the minimum amount of coins that is to be returned to the user
# The user puts in their change requirement in increments of cents

def coin_calc(change):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    # Calculate number of coins to return
    while (change >= 25): # Quarters
        quarters += 1
        change = change - 25
    while (change >= 10): # Dimes
        dimes += 1
        change = change - 10
    while (change >= 5): # Nickels
        nickels += 1
        change = change - 5
    while (change >= 1): # Pennies
        pennies += 1
        change = change - 1

    return(quarters + dimes + nickels + pennies)

def main():
    # Get user input that is an int which is greater than 0
    while True:
        try:
            change = int(input("Change owed: "))
            if change > 0:
                break
            print("Please enter a value greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")
    change_owed = coin_calc(change)
    # Prints result
    print(change_owed)


if __name__ == "__main__":
    main()