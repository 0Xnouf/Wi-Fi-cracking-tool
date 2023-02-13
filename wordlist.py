# importing the required modules
from itertools import product
import string


def generate_wordlist():
    # defining the length of the password
    min_len = int(input("Enter the minimum length of password:- "))
    max_len = int(input("Enter the maximum length of password:- "))
    count = 0
    # using upper & lower case letters, digits, punctuation to produce a wordlist
    character = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    # write the result to a file
    file_open = open("wordlist.txt", "w")

    for i in range(min_len, max_len):
        for j in product(character, repeat=i):
            word = "".join(j)
            file_open.write(word)
            file_open.write("\n")
            count += 1
    print("A new wordlist of {} passwords is created".format(count))
    return "wordlist.txt"
