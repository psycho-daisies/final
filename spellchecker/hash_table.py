"""
Dictionary Program for Midterm
Hash Table class for use in Dictionary Program
By: Troy Brunette
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, word):
        # Simple hash function using the ASCII values of characters in the word
        hash_value = 0
        for char in word:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def insert(self, word):
        index = self.hash_function(str(word))
        if self.table[index] is None:
            self.table[index] = [word]
        else:
            self.table[index].append(word)

    def search(self, word):
        index = self.hash_function(word)
        if self.table[index] is not None:
            return word in self.table[index]
        return False

    def delete(self, word):
        index = self.hash_function(word)
        if self.table[index] is not None and word in self.table[index]:
            self.table[index].remove(word)

    def __contains__(self, word):
        index = self.hash_function(word)

        # Check if the key is in the linked list at the computed index
        if self.table[index] is not None:
            for item in self.table[index]:
                if item == word:
                    return True
        return False

    def get_words(self):
        # Retrieve all words from the hash table
        words = []
        for word in self.table:
            if word is not None:
                words.extend(word)
        return words

