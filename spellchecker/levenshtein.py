import numpy
from read_file import read_file

"""
Dictionary Program for Midterm
By: Troy Brunette

The Levenshtein distance is used for correcting typos and completing words
* Create 2D Matrix: The Distance Matrix
    - dynamic programming approach to calculate Levenshtein distance between two words
* Function levenshtein_distance_matrix
    - accepts 2 arguments: token1 and token2 representing the two words
    - returns an integer representing the distance between them

    - Given two words of lengths m and n, create a 2D matrix of integers of size (m+1, n+1) or (n+1, m+1)
      based on whether the first word represents the rows or the columns
    - the next line creates the matrix in a variable named distances
"""


def levenshtein_distance_matrix(word1, word2):
    """Create 2D Matrix: The Distance Matrix
    - dynamic programming approach to calculate the Levenshtein distance between two words"""
    distances = numpy.zeros((len(word1) + 1, len(word2) + 1))

    for t1 in range(len(word1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(word2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(word1) + 1):
        for t2 in range(1, len(word2) + 1):
            if word1[t1 - 1] == word2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if a <= b and a <= c:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(word1)][len(word2)]


def calc_distance(word, num_words):
    """Calculates the distance between two words and returns a list of words that match"""
    file = read_file("res/1-1000.txt")
    dict_word_dist = []
    word_index = 0

    for line in file:
        word_distance = levenshtein_distance_matrix(word, line.strip())
        if word_distance >= 10:
            word_distance = 9
        dict_word_dist.append(str(int(word_distance)) + "-" + line.strip())
        word_index += 1

    closest_words = []
    word_details = []
    current_word_dist = 0
    dict_word_dist.sort()
    # print(dict_word_dist)
    for i in range(num_words):
        current_word_dist = dict_word_dist[i]
        word_details = current_word_dist.split("-")
        closest_words.append(word_details[1])
    return closest_words
