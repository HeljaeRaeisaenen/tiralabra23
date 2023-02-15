from time import time
from pathlib import Path
from constants import initialize
from trie import Node, Trie
from markov_process import Markov


def main():
    path = 'data/'
    file = input('Give filename: ')
    degree = input('Give degree: ')
    if not degree:
        degree = 4
    try:
        degree = int(degree)
    except:
        print("'Degree' must be a number")
        return
    start_str = input('The sentence should start with: ')

    if 'src' in str(Path('.').resolve()):
        path = '../data/'
    if not file:
        file = 'alice.txt'

    filepath = Path(path+file).resolve()
    initialize(filepath)
    a = time()
    trie = Trie(Node(), degree)
    trie.fill_with_words()
    # print(trie)
    b = time()

    mark = Markov(trie)
    sentence = mark.generate_sentence(start_str, degree)
    if not sentence:
        sentence = 'Try another word or phrase'

    print('\n'+sentence+'\n')
    print(b-a, 's')


main()
