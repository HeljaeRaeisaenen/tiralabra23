'''Holds constants that are needed everywhere in the program, because passing them on gets
complicated.'''
from read_file import read_file


def initialize(path):
    '''Get the sentences in the text file at path. Set constants: a sentences list and an alphabet.
    Args:
        path = path to a file/folder to be read
    Raises:
        EmptyFileException: if the func read_file doesn't return any content for the constant
        SENTENCES, raise this exception, because SENTENCES should have content.'''

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
