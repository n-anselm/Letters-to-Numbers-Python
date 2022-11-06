#!/usr/bin/python

# Author: n-anselm
# Date created: 221105
# Date modified: 221106
# Description: Takes each letter from a string and gets the letter's
# location number in the alphabet, then concatenates the numbers.

def main():
    word = "Python"  # String to convert to numbers
    letter_list = []
    numlist = []
    number = ""

    word = word.lower()  # Convert to lowercase

    # Separate the letters and add to a list
    for letter in word:
        letter_list.append(letter)

    for item in letter_list:
        # Get the ASCII code of the letter minus 96 to get the actual
        # location of the letter in the alphabet
        numlist.append(ord(item) - 96)

    for item in numlist:
        number += str(item)

    print(number)


if __name__ == "__main__":
    main()
