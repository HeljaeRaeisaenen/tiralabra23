from trie import Trie, Node
from index import ALPHABET, sentences
from random import randint

class Markov:
    def __init__(self) -> None:
        self.trie = Trie(Node(), sentences)

    def create_sentence_random(self, start:str):
        '''Create a random sentence from a starting word.
        Args:
            start: starting word'''
        if start not in ALPHABET:
            return False
        
        generated_sentence = []
        word = start
        nodes = self.trie.search_hack(word)
        nodes.union(self.trie.search_hack(word.lower()))
        while True:
            generated_sentence.append(word)
            nodes = self.trie.search_hack(word)
            random_index = randint(0, len(nodes)-1)
            node = list(nodes)[random_index]
            
            
            if node.terminal:
                chance = randint(1,2)
                if (chance % 2) == 0:
                    break
            
            next_words = node.give_children()
            print(len(next_words))
            if len(next_words) == 0:
                break
            random_index = randint(0, len(next_words)-1)
            word = next_words[random_index].value

        return generated_sentence



if __name__ == '__main__':
    mark = Markov()
    s = mark.create_sentence_random('Minä')
    print(s)
