"""Program to check if string is a palindrome"""

def get_string():
    """Get a string from user to be used in function to check for palindrome"""
    # Get string from user with input() and return result 
    user_string = input("Please enter a string to check if it's a palindrome: ")
    return user_string

def check_palindrome(user_string):
    """Reverse string from user and check if palindrome"""
    user_string_reverse = user_string[::-1]
    if user_string_reverse == user_string:
        print("It's a palindrome!")
    else:
        print("It's NOT a palindrome!")

if __name__ == "__main__":
    user_string = get_string()
    check_palindrome(user_string)
