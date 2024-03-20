"""
Troy Brunette
CS240
Final - Recursion: Exponents

Implement a solution using recursion
where the user input a value (x), an exponent (e) and the method generates the result.

"""


def power_recursive(x, e):
    """RECURSIVE VERSION: Calculate x raised to the power of e.

    :param x: The base number
    :param e: The exponent
    :return:  Returns x raised to the power e
    """
    # Base case:
    if e == 0:
        return 1
    # Recursive case: subtract 1 from e and multiply by x
    elif e > 0:
        return x * power_recursive(x, e - 1)
    # Recursive case: for negative exponents, recursive call with 1 added to e and divide by x
    else:
        return (1 / x) * power_recursive(x, e + 1)


def power_iterative(x, e):
    """ITERATIVE VERSION: Calculate x raised to the power of e.

    :param x: The base number
    :param e: The exponent
    :return:  Returns x raised to the power e
    """
    result = 1
    if e >= 0:  # for positive exponents
        for _ in range(e):
            result *= x  # multiply by x each iteration
    else:  # for negative exponents
        for _ in range(-e):
            result /= x  # divide by x each iteration
    return result


# Test Case
base = float(input("Enter the base (x): "))
exp = int(input("Enter the exponent (e): "))

result1 = power_recursive(base, exp)
result2 = power_iterative(base, exp)
print(f"Result: {int(base)}^{exp} = {result1}")
