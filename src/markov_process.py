from random import randint, choices
from itertools import accumulate
from trie import Trie, Node
import constants


class Markov:
    def __init__(self, trie:Trie) -> None:
        self.trie = trie

    def create_sentence_random(self, start: str):
        '''Create a random sentence from a starting word.
        Args:
            start: starting word'''

        word = self.validate_starting_word(start)
        if not word:
            return False
        word = word[0]

        generated_sentence = []
        nodes = self.trie.search_quick(word)
        try:
            nodes.union(self.trie.search_quick(word.lower()))
        except:
            pass
        while True:
            generated_sentence.append(word)
            nodes = self.trie.search_quick(word)
            random_index = randint(0, len(nodes)-1)
            node = list(nodes)[random_index]

            next_words = node.give_children()
            # print(len(next_words))
            if len(next_words) == 0:
                break
            random_index = randint(0, len(next_words)-1)
            word = next_words[random_index].value

        generated_sentence = self.format_sentence(generated_sentence)
        return generated_sentence

    def generate_sentence(self, start: str, degree: int):
        word = self.validate_starting_word(start)
        if not word:
            return False

        generated_sentence = word
        rule = word[-degree:]

        while True:
            print(rule)
            next_nodes = self.trie.search(rule)
            if not next_nodes:
                break
            for node in next_nodes:
                print('next node:', node.value)
            weights = self.calculate_weights(next_nodes)
            chosen_one = choices(next_nodes, cum_weights=weights, k=1)[0]
            print('chosen: ', chosen_one.value)
            generated_sentence.append(chosen_one.value)
            rule = generated_sentence[-degree:]

        # children = next_nodes.give_children()
        # weights = self.calculate_weights(children)
        # print(children, weights)
        # chosen_one = choices(children, cum_weights=weights, k=1)[0]
        # print(chosen_one.value)

        return generated_sentence

    def calculate_weights(self, nodes):
        freqs = [0]*len(nodes)

        index = 0
        for node in nodes:
            freqs[index] = node.freq
            index += 1

        total = sum(freqs)

        for index in range(0, len(nodes)):
            freqs[index] = freqs[index] / total
        freqs = list(accumulate(freqs))
        return freqs

    def validate_starting_word(self, start):
        if ' ' in start:
            start = start.split(' ')
        else:
            start = [start]
        validated = []
        for word in start:
            if word not in constants.ALPHABET:
                if word.lower() in constants.ALPHABET:
                    validated.append(word.lower())
                else:
                    return False
            else:
                validated.append(word)
        return validated

    def format_sentence(self, sentence: list):
        if len(sentence) == 1:
            return sentence[0]

        output = ''
        for word in sentence[:-2]:
            output += word + ' '

        output += sentence[-2] + sentence[-1]

        output = output.capitalize()

        return output


if __name__ == '__main__':
    constants.init('tests/testdata/ilike.txt')
    trie = Trie(Node())
    trie.fill_with_sentences()
    mark = Markov(trie)
    s = mark.generate_sentence('I like', 3)
    print(s)
