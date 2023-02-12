from random import choices
from itertools import accumulate
from trie import Trie, Node
import constants

QUOTE_MARKS = '"“”'


class Markov:
    '''Class that does Markov process.
    Attributes:
        trie: a populated trie structure that contains the rules of the process'''

    def __init__(self, trie: Trie) -> None:
        self.trie = trie

    def generate_sentence(self, start: str, degree: int):
        '''Creates sentence using a Markov process.
        Args:
            start: a word or words that are to start the sentence
            degree: which degree of process to use
        Returns:
            a string sentence generated by the process'''

        word = self.validate_starting_word(start)
        if not word:
            return False

        generated_sentence = word
        rule = word[-degree:]

        open_quote = False
        # if generated_sentence[0][0] in quote_marks:
        #    open_quote = True

        while True:
            # print(rule)
            # print('open quote', open_quote)
            next_words = self.trie.search(rule)
            if not next_words:
                break

            # for node in next_words:
                # print('     next node:', node.value)
            weights = self.calculate_weights(next_words)
            chosen_one = choices(next_words, cum_weights=weights, k=1)[0]
            # print('chosen: ', chosen_one.value, chosen_one.freq)

            generated_sentence.append(chosen_one.value)
            rule = generated_sentence[-degree:]

        return self.format_sentence(generated_sentence, open_quote)

    def calculate_weights(self, nodes):
        '''Determine which of the words does appear more often and should thus be favoured.
        Args:
            nodes: list of trie nodes, representing next possible words in the Markov chain
        Returns:
            probabilities: list of the relative probabilities of each word, calculated by how often
            they have appeared in their context in the source material. used as weights in a random
            choice'''
        probabilities = [0]*len(nodes)

        index = 0
        for node in nodes:
            probabilities[index] = node.freq
            index += 1

        total = sum(probabilities)

        for index in range(0, len(nodes)):
            probabilities[index] = probabilities[index] / total
        probabilities = list(accumulate(probabilities))
        return probabilities

    def validate_starting_word(self, start):
        '''Make sure the starting word/-s is/are in the alphabet, and turn them into a list
        Args:
            start: string containing the starting word(s)
        Returns:
            list containing the starting word(s)'''

        if len(start) == 0:
            start = self.random_word()

        start = start.split(' ')

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

    def format_sentence(self, sentence: list, add_end_quote):
        '''Turn the generated list of words into a string structured like a sentence
        Args:
            sentence: list of strings
        Returns:
            a pretty string'''
        sentence[0] = sentence[0].capitalize()
        if len(sentence) == 1:
            return sentence[0]

        output = ''
        for word in sentence[:-2]:
            # if word in QUOTE_MARKS:
            #    output = output[:-1]
            output += word + ' '

        output += sentence[-2] + sentence[-1]

        if add_end_quote:
            output += '”'

        return output

    def random_word(self):
        '''Get a random word of the alphabet that can start a three-word sequence.
        Returns: string'''
        possible_starts = self.trie.root.give_children()
        chosen = choices(possible_starts, k=1)[0]
        if len(chosen.value) != 1:
            if chosen.value[-1] in QUOTE_MARKS or chosen.value[-2] in QUOTE_MARKS:
                print('NO')
                return self.random_word()

        return chosen.value


if __name__ == '__main__':
    constants.init('tests/testdata/catsanddogs.txt')
    trie = Trie(Node())
    trie.fill_with_words()
    mark = Markov(trie)
    s = mark.generate_sentence('i', 2)
    print(s)
