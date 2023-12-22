""" count the letters shakespear used """
from matplotlib import pyplot


def main():

    letters_count = read_char("data/shakespeare.txt")
    char_chart(letters_count)


def read_char(file):
    """ read the content of a file then count the characters """
    count = {}
    file_handle = open(file, 'r')
    for line in file_handle:
        for char in line.lower():
            if char.isalpha():
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1

    file_handle.close()
    return count


def char_chart(letters_count):
    pyplot.title("frequencies of all the letters used by Shakespear")
    pyplot.xlabel("Letters")
    pyplot.ylabel("Frequency")
    labels = list(letters_count.keys())
    values = list(letters_count.values())
    pyplot.bar(labels, values)
    pyplot.show()


main()