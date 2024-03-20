"""
Troy Brunette
CS240
Recursion: Convert an integer to a Binary number

Implement a solution for converting an integer to a binary number using recursion.
Please include an algorithm with pseudo-code, as well as source code in the language of your choice.

Convert to binary Algorithm:

* If the number is 0, it returns an empty string.
* For non-zero numbers, it recursively calls itself on the quotient of the number divided by 2.
* It then concatenates the remainder of the division (0 or 1) to the result of the recursive call.
* This process continues until the number becomes 0, at which point the function starts returning
  the binary representation by concatenating the remainders in reverse order.


Now compare the efficiency of each (iteration versus recursion).  What is the efficiency of each.
"""
