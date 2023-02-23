'''Holds constants that are needed everywhere in the program, because passing them on gets
complicated.'''
from read_file import read_file

def initialize(path):
    '''Get the sentences in the text file at path. Make a sentences list and an alphabet.'''
    global SENTENCES
    SENTENCES = []

    global ALPHABET
    ALPHABET = set()
    
    SENTENCES = SENTENCES + read_file(path)

    ALPHABET.update(*SENTENCES)

    if len(SENTENCES) == 0:
        raise EmptyFileException

class EmptyFileException(Exception):
    '''Raise when the file given by user is empty or the text inside is unusable,
    for example, if it doesn't contain sentences.'''
    pass