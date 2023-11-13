MAX_LINES = 3

# Setup the amount the customer wants to deposit for play with an input prompt.
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
           amount = int(amount)
        if amount > 0:
            break
        else:
            print("Amount must be greater than 0")
    else:
        print("Please enter a number?")
            
    return amount

# Create a function that the user determines how many lines they want to bet on
def get_num_of_lines():
    while True:
        lines = input("How many lines do you wanna bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(line)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Pick how many lines... 1, 2 or 3")
        else:
            print("Please enter a number?")
    return lines

def main():
    balance = deposit()
    lines = get_num_of_lines()
    print(balance, lines)