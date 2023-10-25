def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Input the number of terms you want in the series
n = int(input("Enter the number of Fibonacci terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = generate_fibonacci(n)
    print("Fibonacci series:")
    for term in result:
        print(term)
