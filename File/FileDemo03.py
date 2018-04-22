""" count word frequency """

import sys
import os

def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        printf("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    table = {}
    with open(filepath, 'r') as fp:
        for index, line in enumerate(fp, start = 1):
            print("Line {} contents {}".format(index, line.strip()))
            record_word_cnt(line.strip().split(' '), table)
    sorted_words = sort_word_by_occurrance(table, desc=True)
    print("Most frequent 10 words:", sorted_words[:10])

def record_word_cnt(words, table):
    for word in words:
        if word:
            if word.lower() not in table:
                table[word.lower()] = 0
            table[word.lower()] += 1 

def sort_word_by_occurrance(table, desc=False):
    words = [(word, count) for word, count in table.items()]
    return sorted(words, key = lambda x:x[1], reverse=True)

if __name__ == '__main__':
    main()