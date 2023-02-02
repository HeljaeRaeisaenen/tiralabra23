'''Holds constants that are needed everywhere in the program, because passing them on gets
complicated.'''
from read_file import read_file


def init(path):
    '''Get the sentences in the text file at path. Make a sentences list and an alphabet.'''
    global SENTENCES
    SENTENCES = read_file(path)
    global ALPHABET
    ALPHABET = set()
    ALPHABET.update(*SENTENCES)
