"""
Dictionary Program for Midterm
By: Troy Brunette

The user can type a word and find out if it's in the stored list of words.
If the word is not in the table, some suggested words are printed.
Uses Levenshtein Distance Algorithm to suggest word corrections
For implementing The Levenshtein Distance:
- I followed along with this website to implement the algorithm
    - https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
- The list of words I used came from:
    - '1000 Most Common US English words:'
    - https://gist.github.com/deekayen/4148741

Contains functions for:
    - reading from a text file
    - create hash table and add words from a text file
    - check the table for a user specified word
    - add words to a list of words
"""
from hash_table import HashTable
from levenshtein import calc_distance, read_file
from read_file import get_menu_border


# Main part of program
def main():
    hash_table, words_list = get_words_from_file()
    display_menu()

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("Importing from file...")
            hash_table, words_list = get_words_from_file()
            print("Import Complete")

        elif choice == '2':
            user_word_list, hash_table = add_user_word(hash_table)
            print("The words you added: ", user_word_list)

        elif choice == '3':
            word = input("Enter a word to check: ")
            if hash_table and hash_table.__contains__(word):
                print(f"{word} is in the table.")
            elif not hash_table.__contains__(word):
                closest = calc_distance(word, 3)
                print(f"{word} is not in the Dictionary. Did you mean to type? {closest} ")

        elif choice == '4':
            print("Program Exit")
            break
        else:
            print(f"Invalid choice. Please Enter Choice: (1-4): ")


# Reads from a text file that contains the Menu
def display_menu():
    # Example usage:
    file_path = 'res/borders.txt'  # Replace 'your_file.txt' with the path to your text file
    lines = get_menu_border(file_path)

    # Print the lines or perform any other operations with the lines array
    for line in lines:
        print(line)


def add_user_word(hash_table):
    """Asks user for words to add to the table"""
    word_list = []

    while True:
        user_input = input("Enter a word (or type 'stop' to end): ")

        if user_input.lower() == 'stop':
            break  # Exit the loop if the user enters 'stop'
        else:
            if hash_table.__contains__(user_input):
                print(f"{user_input} is already a word in the table!")
            else:
                word_list.append(user_input)
                hash_table.insert(user_input)
                print(f"{user_input} added to the list.\n")

    # print("The words you entered:", word_list)
    return word_list, hash_table


# Reads from a text file and adds the words to a HashTable
def get_words_from_file():
    hash_table = HashTable(size=1500)
    words = read_file("res/1-1000.txt")
    for word in words:
        hash_table.insert(word.strip())

    return hash_table, words


# Entry to program
main()
