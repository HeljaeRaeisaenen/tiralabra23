from read_file import read_file

sentences = read_file('tests/testdata/catsanddogs.txt') #../data/alice.txt
ALPHABET = set()
ALPHABET.update(*sentences)


#print(sentences)
print(ALPHABET)
