"""Program to check all divisors of a positive integer"""

def get_number():
    """Get a number from user, convert to integer,
    and return the value"""
    # Get number, this will be a string
    number = input("Please enter a positive integer: ")
    # Convert string to an integer
    number_int = int(number)
    # Return the number
    return number_int

def create_list(number_int):
    """Create list consisting of all numbers from zero
    to user-specified number, to find divisors"""
    # Create list using range, user number plus 1 is end number
    mylist = list(range(1, (number_int + 1)))
    # Return the list
    return mylist

def check_divisor(mylist):
    """Take a list and check for all divisors"""
    # Create empty list to store divisors
    divisors = []
    # Loop through the list
    for number in mylist:
        # Check if modulo is 0, then divisor is found
        if (mylist[-1] % number == 0):
            # When divisor found, add to list
            divisors.append(number)
    # Print all divisors
    for divisor in divisors:
        print(divisor)

# Run code if not imported as module
if __name__ == "__main__":
    number_int = get_number()
    mylist = create_list(number_int)
    check_divisor(mylist)
