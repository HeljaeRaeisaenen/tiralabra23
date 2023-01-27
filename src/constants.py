'''Holds varaibles that are needed everywhere. Passing them onto class instances gets messy.
Nowhere is the probram supposed to alter these values.'''
from read_file import read_file


def init(path):
    global SENTENCES
    SENTENCES = read_file(path)  # tests/testdata/catsanddogs.txt
    global ALPHABET
    ALPHABET = set()
    ALPHABET.update(*SENTENCES)
