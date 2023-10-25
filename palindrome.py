def is_palindrome(input_str):
    # Remove spaces and convert the string to lowercase
    input_str = input_str.replace(" ", "").lower()

    # Compare the original string with its reverse
    return input_str == input_str[::-1]

# Input from the user
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
