from mylib import *
from calCLI import *
from click.testing import CliRunner
import pytest

"""
# what are the steps for writing test for cli in calCLI.py
# 1. Import necessary modules and functions.
# 2. Create a test function for each CLI command.
# 3. Use the `CliRunner` to invoke the CLI command.
# 4. Check the output and return code using assertions.

- Addition
- Subtraction
- Multiplication
- Division
- Square
- Square Root
- Power
- Factorial
- gcd
- lcm
- is_prime
- fibonacci
- factorial_iterative
- factorial_recursive
- is_even
- is_odd
- prime_factorization

"""

# write the test for each command in calCLI.py
# add_command
def test_add_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "3", "5"])
    assert result.exit_code == 0
    assert "The result of adding 3.0 and 5.0 is: 8.0" in result.output
    assert "green" in result.output

# subtract_command
def test_subtract_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["subtract", "10", "4"])
    assert result.exit_code == 0
    assert "The result of subtracting 4.0 from 10.0 is: 6.0" in result.output
    assert "green" in result.output

# multiply_command
def test_multiply_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["multiply", "6", "7"])
    assert result.exit_code == 0
    assert "The result of multiplying 6.0 and 7.0 is: 42.0" in result.output
    assert "red" in result.output

# divide_command
def test_divide_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["divide", "8", "2"])
    assert result.exit_code == 0
    assert "The result of dividing 8.0 by 2.0 is: 4.0" in result.output
    assert "green" in result.output

# test for divide by zero
def test_divide_by_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["divide", "8", "0"])
    assert result.exit_code != 0
    assert "Cannot divide by zero" in result.output
    assert "red" in result.output

# test for square
def test_square_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["square", "4"])
    assert result.exit_code == 0
    assert "The square of 4.0 is: 16.0" in result.output
    assert "green" in result.output

# test for square root
def test_square_root_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["square_root", "16"])
    assert result.exit_code == 0
    assert "The square root of 16.0 is: 4.0" in result.output
    assert "green" in result.output

# test for square root of negative number
def test_square_root_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["square_root", "-16"])
    assert result.exit_code != 0
    assert "Cannot calculate square root of negative number" in result.output
    assert "red" in result.output

# test for power
def test_power_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert "The result of raising 2.0 to the power of 3.0 is: 8.0" in result.output
    assert "green" in result.output

# test for factorial
def test_factorial_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial", "5"])
    assert result.exit_code == 0
    assert "The factorial of 5.0 is: 120.0" in result.output
    assert "green" in result.output

# test for factorial of negative number
def test_factorial_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial", "-5"])
    assert result.exit_code != 0
    assert "Cannot calculate factorial of negative number" in result.output
    assert "red" in result.output

# test for factorial of 0
def test_factorial_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial", "0"])
    assert result.exit_code == 0
    assert "The factorial of 0.0 is: 1.0" in result.output
    assert "green" in result.output

# test for factorial of 1
def test_factorial_one():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial", "1"])
    assert result.exit_code == 0
    assert "The factorial of 1.0 is: 1.0" in result.output
    assert "green" in result.output

# test for gcd
def test_gcd_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["gcd", "48", "18"])
    assert result.exit_code == 0
    assert "The GCD of 48.0 and 18.0 is: 6.0" in result.output
    assert "green" in result.output

# test for lcm
def test_lcm_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["lcm", "4", "6"])
    assert result.exit_code == 0
    assert "The LCM of 4.0 and 6.0 is: 12.0" in result.output
    assert "green" in result.output

# test for lcm of 0
def test_lcm_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["lcm", "0", "6"])
    assert result.exit_code != 0
    assert "Cannot calculate LCM of zero" in result.output
    assert "red" in result.output

# test for lcm of negative number
def test_lcm_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["lcm", "-4", "6"])
    assert result.exit_code != 0
    assert "Cannot calculate LCM of negative number" in result.output
    assert "red" in result.output

# test for prime
def test_is_prime_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_prime", "7"])
    assert result.exit_code == 0
    assert "7 is a prime number." in result.output
    assert "yellow" in result.output

# test for prime number
def test_is_prime_not_prime():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_prime", "8"])
    assert result.exit_code == 0
    assert "8 is not a prime number." in result.output
    assert "yellow" in result.output

# test for prime number negative
def test_is_prime_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_prime", "-7"])
    assert result.exit_code != 0
    assert "-7 is not a prime number." in result.output
    assert "red" in result.output

# test for prime number 1
def test_is_prime_one():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_prime", "1"])
    assert result.exit_code != 0
    assert "1 is not a prime number." in result.output
    assert "red" in result.output

# test for prime number 2
def test_is_prime_two():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_prime", "2"])
    assert result.exit_code == 0
    assert "2 is a prime number." in result.output
    assert "yellow" in result.output

# test for prime number 0
def test_is_prime_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_prime", "0"])
    assert result.exit_code != 0
    assert "0 is not a prime number." in result.output
    assert "yellow" in result.output

# test for fibonacci
def test_fibonacci_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["fibonacci", "5"])
    assert result.exit_code == 0
    assert "The Fibonacci sequence up to 5 is: [0.0, 1.0, 1.0, 2.0, 3.0, 5.0]" in result.output
    assert "green" in result.output

# test for fibonacci negative
def test_fibonacci_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["fibonacci", "-5"])
    assert result.exit_code != 0
    assert "Cannot generate Fibonacci sequence for negative number" in result.output
    assert "red" in result.output

# test for fibonacci 0
def test_fibonacci_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["fibonacci", "0"])
    assert result.exit_code == 0
    assert "The Fibonacci sequence up to 0 is: [0.0]" in result.output
    assert "green" in result.output

# test for fibonacci 1
def test_fibonacci_one():
    runner = CliRunner()
    result = runner.invoke(cli, ["fibonacci", "1"])
    assert result.exit_code == 0
    assert "The Fibonacci sequence up to 1 is: [0.0, 1.0]" in result.output
    assert "green" in result.output

# test for factorial iterative
def test_factorial_iterative_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial_iterative", "5"])
    assert result.exit_code == 0
    assert "The factorial of 5 (iterative) is: 120.0" in result.output
    assert "magenta" in result.output

# test for factorial iterative negative
def test_factorial_iterative_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial_iterative", "-5"])
    assert result.exit_code != 0
    assert "Cannot calculate factorial of negative number" in result.output
    assert "red" in result.output

# test for factorial iterative 0
def test_factorial_iterative_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial_iterative", "0"])
    assert result.exit_code == 0
    assert "The factorial of 0 (iterative) is: 1.0" in result.output
    assert "magenta" in result.output

# test for factorial iterative 1
def test_factorial_iterative_one():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial_iterative", "1"])
    assert result.exit_code == 0
    assert "The factorial of 1 (iterative) is: 1.0" in result.output
    assert "magenta" in result.output

# test for factorial recursive
def test_factorial_recursive_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial_recursive", "5"])
    assert result.exit_code == 0
    assert "The factorial of 5 (recursive) is: 120.0" in result.output
    assert "green" in result.output

# test for factorial recursive negative
def test_factorial_recursive_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["factorial_recursive", "-5"])
    assert result.exit_code != 0
    assert "Cannot calculate factorial of negative number" in result.output
    assert "red" in result.output

# test for is_even
def test_is_even_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_even", "4"])
    assert result.exit_code == 0
    assert "4 is even number." in result.output
    assert "red" in result.output

# test for is_even negative number
def test_is_even_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_even", "-4"])
    assert result.exit_code == 0
    assert "-4 is even number." in result.output
    assert "red" in result.output

# test for is_odd
def test_is_odd_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_odd", "5"])
    assert result.exit_code == 0
    assert "5 is odd number." in result.output
    assert "red" in result.output

# test for is_odd negative number
def test_is_odd_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["is_odd", "-5"])
    assert result.exit_code == 0
    assert "-5 is odd number." in result.output
    assert "red" in result.output

# test for prime factorization
def test_prime_factorization_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["prime_factorization", "28"])
    assert result.exit_code == 0
    assert "The prime factorization of 28 is: [2.0, 2.0, 7.0]" in result.output
    assert "green" in result.output

# test for prime factorization negative number
def test_prime_factorization_negative():
    runner = CliRunner()
    result = runner.invoke(cli, ["prime_factorization", "-28"])
    assert result.exit_code != 0
    assert "Cannot calculate prime factorization of number less than 2" in result.output
    assert "red" in result.output
    
