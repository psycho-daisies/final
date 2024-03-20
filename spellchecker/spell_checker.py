"""
Troy Brunette
CS240
Final - Spell Checker (50 points)

Create a spell checker console program that uses a hash table data structure to store a dictionary of words. Your program should be able to:

Load a dictionary of words from a file into the hash table.

Take a string of text as input and check each word in the text against the words in the dictionary stored in the hash table. Your program should identify any words that are not found in the dictionary and display them as "misspelled".

Implement a suggestion feature that suggests possible correct spellings for the misspelled words based on edit distance.

Implement a Levenshtein distance algorithm to compute the edit distance between two words.

Allow the user to add new words to the dictionary and update the hash table accordingly.

Handle collisions in the hash table using separate chaining.

Optimize the performance of your program in terms of time and space complexity.
Your program should be user-friendly and have a command-line interface.
"""
