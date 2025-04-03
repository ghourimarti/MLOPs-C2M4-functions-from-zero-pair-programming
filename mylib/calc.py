"""
A calculator module that provides basic arithmetic operations.
This module includes functions for addition, subtraction, multiplication, and division.
It also includes a function to calculate the square of a number.
The functions are designed to handle both integers and floats.
The functions raise ValueError for invalid inputs.
The functions are designed to be used in a simple calculator application.
The functions are:
- add: Adds two numbers.
- subtract: Subtracts the second number from the first.
- multiply: Multiplies two numbers.
- divide: Divides the first number by the second.
- square: Calculates the square of a number.
- square_root: Calculates the square root of a number.
- power: Raises a number to the power of another number.
- factorial: Calculates the factorial of a number.
- gcd: Calculates the greatest common divisor of two numbers.
- lcm: Calculates the least common multiple of two numbers.
- is_prime: Checks if a number is prime.
- fibonacci: Generates a Fibonacci sequence up to a given number.
- factorial_iterative: Calculates the factorial of a number iteratively.
- factorial_recursive: Calculates the factorial of a number recursively.
- is_even: Checks if a number is even.
- is_odd: Checks if a number is odd.
- prime_factorization: Calculates the prime factorization of a number.
This module is designed to be used in a simple calculator application.
This module is part of the mylib package.
"""


# Addition function
def add(a, b):
    """
    Adds two numbers.
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b


# Subtraction function
def subtract(a, b):
    """
    Subtracts the second number from the first.
    :param a: First number
    :param b: Second number
    :return: Difference of a and b
    """
    return a - b


# Multiplication function
def multiply(a, b):
    """
    Multiplies two numbers.
    :param a: First number
    :param b: Second number
    :return: Product of a and b
    """
    return a * b


# Division function
def divide(a, b):
    """
    Divides the first number by the second.
    :param a: First number
    :param b: Second number
    :return: Quotient of a and b
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Square function
def square(a):
    """
    Calculates the square of a number.
    :param a: Number to be squared
    :return: Square of a
    """
    return a**2


# Square root function
def square_root(a):
    """
    Calculates the square root of a number.
    :param a: Number to find the square root of
    :return: Square root of a
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a**0.5


# Power function
def power(a, b):
    """
    Raises a number to the power of another number.
    :param a: Base number
    :param b: Exponent
    :return: a raised to the power of b
    """
    return a**b


# Factorial function
def factorial(n):
    """
    Calculates the factorial of a number.
    :param n: Number to find the factorial of
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# GCD function
def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers.
    :param a: First number
    :param b: Second number
    :return: GCD of a and b
    """
    while b:
        a, b = b, a % b
    return a


# LCM function
def lcm(a, b):
    """
    Calculates the least common multiple of two numbers.
    :param a: First number
    :param b: Second number
    :return: LCM of a and b
    """
    return abs(a * b) // gcd(a, b)


# Prime check function
def is_prime(n):
    """
    Checks if a number is prime.
    :param n: Number to check
    :return: True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Fibonacci function
def fibonacci(n):
    """
    Generates a Fibonacci sequence up to a given number.
    :param n: Number to generate Fibonacci sequence up to
    :return: List of Fibonacci numbers
    """
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:-1]  # Exclude the last number if it exceeds n


# Factorial iterative function
def factorial_iterative(n):
    """
    Calculates the factorial of a number iteratively.
    :param n: Number to find the factorial of
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Factorial recursive function
def factorial_recursive(n):
    """
    Calculates the factorial of a number recursively.
    :param n: Number to find the factorial of
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Even check function
def is_even(n):
    """
    Checks if a number is even.
    :param n: Number to check
    :return: True if n is even, False otherwise
    """
    return n % 2 == 0


# Odd check function
def is_odd(n):
    """
    Checks if a number is odd.
    :param n: Number to check
    :return: True if n is odd, False otherwise
    """
    return n % 2 != 0


# Prime factorization function
def prime_factorization(n):
    """
    Calculates the prime factorization of a number.
    :param n: Number to find the prime factorization of
    :return: List of prime factors
    """
    if n < 2:
        raise ValueError("Cannot calculate prime factorization of number less than 2")
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors
