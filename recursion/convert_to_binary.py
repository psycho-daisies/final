"""
Troy Brunette
CS240
Recursion: Convert an integer to a Binary number

Implement a solution for converting an integer to a binary number using recursion.
Please include an algorithm with pseudo-code, as well as source code in the language of your choice.

Convert to binary Algorithm:
* If the number is 0, it returns an empty string.
* If non-zero number, recursively call function on quotient divided by 2.
* join the remainder of the division (0 or 1) to the result of the recursive call.
* continue until the base case is reached and join the remainders in reverse order

PSEUDO-CODE:
def convert_to_binary(n)
    if n = 0
        return ""
    else
        # Recursively call the function on the quotient
        return convert_to_binary(n // 2) + str(n % 2)

"""
import time

def convert_to_binary_recur(n: int):
    """RECURSIVE VERSION: Convert an Integer to a Binary Number."""
    # Base case: If the number is 0, return an empty string
    if n == 0:
        return ""
    else:
        # Recursively call the function on the quotient
        return convert_to_binary_recur(n // 2) + str(n % 2)


# Convert to Binary Iterative
def convert_to_binary_iter(n: int):
    """ITERATIVE VERSION: Convert an Integer to a Binary Number."""
    binary = ""

    # Edge case: If n is 0, binary representation is 0
    if n == 0:
        return "0"

    while n > 0:
        # Get the remainder of n when divided by 2
        remainder = n % 2
        # Add the remainder to the beginning of the binary number
        binary = str(remainder) + binary
        # Integer divide n by 2 for the next iteration
        n //= 2

    return binary


def in_progress(message, duration, period_length, dots):
    total_periods = int(duration / period_length)

    for i in range(total_periods):
        print(f"{message}", end="", flush=True)
        dots_to_print = min(i % (dots + 1), dots)
        print("." * dots_to_print, end="", flush=True)
        time.sleep(period_length / dots)

        print("\r", end="", flush=True)

    print("\nCalculation Complete.")
    print("=" * 30)  # Optional separator between files


# Test Case
num = int(input("Enter a number to convert to Binary: "))
result = convert_to_binary_recur(num)
in_progress("Calculating", 4, 1, dots=3)
print(f"{num} converted to Binary: {result} ")
