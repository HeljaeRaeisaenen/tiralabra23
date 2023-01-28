from time import time
from pathlib import Path
from constants import init
from trie import Node, Trie
from markov_process import Markov


def main():
    path = 'data/'
    file = input('Syötä tiedoston nimi: ')
    start_str = input('Syötä lauseen aloittava sana: ')

    if 'src' in str(Path('.').resolve()):
        path = '../data/'
    if not file:
        file = 'viehattava.txt'

    filepath = Path(path+file).resolve()
    init(filepath)
    a = time()
    # print(sentences)
    # print(ALPHABET)
    trie = Trie(Node())
    trie.fill_with_sentences()
    #print(trie)
    mark = Markov(trie)
    s = mark.create_sentence_random(start_str or 'Minä')
    if not s:
        s = 'Kokeile eri sanaa'
    
    print('\n'+s+'\n')
    b = time()
    print(b-a, 's')


main()

# '../data/alice.txt'
