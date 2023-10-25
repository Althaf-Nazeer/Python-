def is_armstrong_number(number):
    # Calculate the number of digits in the given number
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the number is an Armstrong number
    return number == sum_of_digits

# Input from the user
user_input = input("Enter a number: ")

try:
    number = int(user_input)
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")
