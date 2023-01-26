
from read_file import read_file

sentences = read_file('../data/viehattava.txt') #tests/testdata/catsanddogs.txt
ALPHABET = set()
ALPHABET.update(*sentences)


#print(sentences)
#print(ALPHABET)
