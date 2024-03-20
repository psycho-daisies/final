"""
Troy Brunette
CS240
Final - Recursion: Least Common Denominator (LCD)

Implement a solution for finding the least common denominator (LCD) of an expression using recursion.
Pass in an integer numerator, and integer denominator value.  Your choice of language.

PSEUDO-CODE:
def gcd(a, b)
    while a ≠ b
        if a > b
            a := a − b
        else
            b := b − a
    return a

def gcd(a, b)
    if b = 0
        return a
    else
        return gcd(b, a mod b)
"""


def gcd_recursive(a: int, b: int) -> int:
    """Uses Recursion to find the Greatest Common Divisor of two integers.
    :return: Returns the GCD of a & b
    """
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def gcd(a: int, b: int) -> int:
    """Finds the Greatest Common Divisor of two integers iteratively.
    Iterative Subtraction-based version of Euclid's algorithm.
    :return: Returns the GCD of a & b"""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# Formula for LCM: (a * b) / GCD(a, b)
def lcm(a, b):
    """Function to find the least common multiple (LCM)."""
    return a * b // gcd(a, b)


def lcd(a, b):
    """Function to find the least common denominator (LCD) of a fraction."""
    return lcm(abs(a), abs(b))


# Test Case:
num1 = 12
num2 = 18
print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")
print(f"LCM of {num1} and {num2}: {lcm(num1, num2)}")
