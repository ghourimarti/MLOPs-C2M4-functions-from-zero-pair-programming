#!/usr/bin/env python3
from mylib.calc import (
    add,
    subtract,
    multiply,
    divide,
    square,
    square_root,
    power,
    factorial,
    gcd,
    lcm,
    is_prime,
    fibonacci,
    factorial_iterative,
    factorial_recursive,
    is_even,
    is_odd,
    prime_factorization,
)
import click

# This module is part of the mylib package.
# This is a simple calculator CLI that performs basic arithmetic operations.
# - Addition
# - Subtraction
# - Multiplication
# - Division
# - Square
# - Square Root
# - Power
# - Factorial
# - gcd
# - lcm
# - is_prime
# - fibonacci
# - factorial_iterative
# - factorial_recursive
# - is_even
# - is_odd
# - prime_factorization


@click.group()
def cli():
    """Simple calculator CLI."""


# Addition command
@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    """Add two numbers.
    :param a: First number
    :param b: Second number
    :return: Sum of a and b

    Example: ./calCLI.py add 3 5
    """
    result = add(a, b)
    click.secho(f"The result of adding {a} and {b} is: {result}", fg="green")


# Subtraction command
@cli.command("subtract")
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract_command(a, b):
    """Subtract two numbers.
    :param a: First number
    :param b: Second number
    :return: Difference of a and b

    Example: ./calCLI.py subtract 10 4
    """
    result = subtract(a, b)
    click.secho(f"The result of subtracting {b} from {a} is: {result}", fg="green")


# Multiplication command
@cli.command("multiply")
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply_command(a, b):
    """Multiply two numbers.
    :param a: First number
    :param b: Second number
    :return: Product of a and b

    Example: ./calCLI.py multiply 6 7
    """
    result = multiply(a, b)
    click.secho(f"The result of multiplying {a} and {b} is: {result}", fg="red")


# Division command
@cli.command("divide")
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide_command(a, b):
    """Divide two numbers.
    :param a: First number
    :param b: Second number
    :return: Quotient of a and b

    Example: ./calCLI.py divide 8 2
    """
    try:
        result = divide(a, b)
        click.secho(f"The result of dividing {a} by {b} is: {result}", fg="blue")
    except ValueError as e:
        click.secho(str(e), fg="red")


# Square command
@cli.command("square")
@click.argument("a", type=float)
def square_command(a):
    """Square a number.
    :param a: Number to be squared
    :return: Square of a

    Example: ./calCLI.py square 4
    """
    result = square(a)
    click.secho(f"The square of {a} is: {result}", fg="yellow")


# Square root command
@cli.command("square_root")
@click.argument("a", type=float)
def square_root_command(a):
    """Square root of a number.
    :param a: Number to find the square root of
    :return: Square root of a

    Example: ./calCLI.py square_root 16
    """
    result = square_root(a)
    click.secho(f"The square root of {a} is: {result}", fg="cyan")


# Power command
@cli.command("power")
@click.argument("a", type=float)
@click.argument("b", type=float)
def power_command(a, b):
    """Power of a number.
    :param a: Base number
    :param b: Exponent
    :return: a raised to the power of b

    Example: ./calCLI.py power 2 3
    """
    result = power(a, b)
    click.secho(f"{a} raised to the power of {b} is: {result}", fg="magenta")


# Factorial command
@cli.command("factorial")
@click.argument("n", type=int)
def factorial_command(n):
    """Factorial of a number.
    :param n: Number to find the factorial of
    :return: Factorial of n

    Example: ./calCLI.py factorial 5
    """
    result = factorial(n)
    click.secho(f"The factorial of {n} is: {result}", fg="green")


# GCD command
@cli.command("gcd")
@click.argument("a", type=int)
@click.argument("b", type=int)
def gcd_command(a, b):
    """GCD of two numbers.
    :param a: First number
    :param b: Second number
    :return: GCD of a and b

    Example: ./calCLI.py gcd 48 18
    """
    result = gcd(a, b)
    click.secho(f"The GCD of {a} and {b} is: {result}", fg="red")


# LCM command
@cli.command("lcm")
@click.argument("a", type=int)
@click.argument("b", type=int)
def lcm_command(a, b):
    """LCM of two numbers.
    :param a: First number
    :param b: Second number
    :return: LCM of a and b

    Example: ./calCLI.py lcm 4 6
    """
    result = lcm(a, b)
    click.secho(f"The LCM of {a} and {b} is: {result}", fg="blue")


# Prime check command
@cli.command("is_prime")
@click.argument("n", type=int)
def is_prime_command(n):
    """Check if a number is prime.
    :param n: Number to check
    :return: True if n is prime, False otherwise

    Example: ./calCLI.py is_prime 7
    """
    result = is_prime(n)
    click.secho(f"{n} is {'a prime' if result else 'not a prime'} number.", fg="yellow")


# Fibonacci command
@cli.command("fibonacci")
@click.argument("n", type=int)
def fibonacci_command(n):
    """Fibonacci sequence up to n.
    :param n: Number of terms in the Fibonacci sequence
    :return: Fibonacci sequence up to n

    Example: ./calCLI.py fibonacci 10
    """
    result = fibonacci(n)
    click.secho(f"The Fibonacci sequence up to {n} is: {result}", fg="cyan")


# Factorial iterative command
@cli.command("factorial_iterative")
@click.argument("n", type=int)
def factorial_iterative_command(n):
    """Factorial of a number (iterative).
    :param n: Number to find the factorial of
    :return: Factorial of n

    Example: ./calCLI.py factorial_iterative 5
    """
    result = factorial_iterative(n)
    click.secho(f"The factorial of {n} (iterative) is: {result}", fg="magenta")


# Factorial recursive command
@cli.command("factorial_recursive")
@click.argument("n", type=int)
def factorial_recursive_command(n):
    """Factorial of a number (recursive).
    :param n: Number to find the factorial of
    :return: Factorial of n

    Example: ./calCLI.py factorial_recursive 5
    """
    result = factorial_recursive(n)
    click.secho(f"The factorial of {n} (recursive) is: {result}", fg="green")


# Even check command
@cli.command("is_even")
@click.argument("n", type=int)
def is_even_command(n):
    """Check if a number is even.
    :param n: Number to check
    :return: True if n is even, False otherwise

    Example: ./calCLI.py is_even 4
    """
    result = is_even(n)
    click.secho(f"{n} is {'even' if result else 'not even'} number.", fg="red")


# Odd check command
@cli.command("is_odd")
@click.argument("n", type=int)
def is_odd_command(n):
    """Check if a number is odd.
    :param n: Number to check
    :return: True if n is odd, False otherwise

    Example: ./calCLI.py is_odd 5
    """
    result = is_odd(n)
    click.secho(f"{n} is {'odd' if result else 'not odd'} number.", fg="blue")


# Prime factorization command
@cli.command("prime_factorization")
@click.argument("n", type=int)
def prime_factorization_command(n):
    """Prime factorization of a number.
    :param n: Number to find the prime factorization of
    :return: List of prime factors

    Example: ./calCLI.py prime_factorization 28
    """
    result = prime_factorization(n)
    click.secho(f"The prime factorization of {n} is: {result}", fg="yellow")


if __name__ == "__main__":
    cli()
# This code is a command-line interface (CLI) for a calculator library.
# It uses the Click library to create a user-friendly interface for performing various mathematical operations.
# The CLI includes commands for addition, subtraction, multiplication, division, square, square root, power, factorial,
# GCD, LCM, prime check, Fibonacci sequence, factorial (iterative and recursive), even check, odd check, and prime factorization.
# Each command has its own function that takes the required arguments and performs the corresponding operation.
# The results are printed to the console with appropriate formatting.
# The CLI is designed to be easy to use and provides helpful error messages for invalid inputs.
# The code is well-structured and follows best practices for creating a command-line interface.
# The use of Click allows for easy customization and extension of the CLI in the future.
# The code is also modular, with the calculator functions being imported from a separate module (mylib.calc).
# This separation of concerns makes the code more maintainable and easier to understand.
