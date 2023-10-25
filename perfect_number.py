def is_perfect_number(number):
    divisors_sum = sum([i for i in range(1, number) if number % i == 0])
    return divisors_sum == number

# Input from the user
user_input = input("Enter a number: ")

try:
    number = int(user_input)
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")
except ValueError:
    print("Please enter a valid integer.")
