__author__ = 'JoaoVictor'

import fileinput
import re
import string


def main():

    file = open('Input03.txt', 'r')
    words = []

    pattern = re.compile('[\W_]+')

    for line in file:
        pattern.sub('', line)
        words += line.split(" ")

    words = [w.split('\n')[0] for w in words]

    print(words)

    # for word1 in words:


if __name__ == "__main__":
    main()
