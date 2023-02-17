from time import time
from pathlib import Path
from constants import initialize
from trie import Node, Trie
from markov_process import Markov

class UI:
    def __init__(self) -> None:
        self._degree = None
        self._starting_word = None

    def _start_process(self):
        while True:
            success = self._open_file()
            if not success:
                return
            self._get_degree()
            self._get_word()
            result = self._get_sentence()
            print('\n'+result+'\n')

    def _open_file(self):
        path = 'data/'
        file = input('Give filename: ')

        if 'src' in str(Path('.').resolve()):
            path = '../data/'
        if not file:
            file = 'alice.txt'
        if file[-4:] != '.txt':
            file += '.txt'

        filepath = Path(path+file).resolve()
        
        try:
            initialize(filepath)
            return True
        except FileNotFoundError:
            print(f'\nCouldn\'t find a file called {file}, make sure that it is in the correct place.\n')
            return False
    
    def _get_degree(self):
        degree = input('Give degree: ')
        if not degree:
            degree = 2
        try:
            self._degree = int(degree)
        except:
            print("'Degree' must be a number")
            return
    
    def _get_word(self):
        self._starting_word = input('The sentence should start with: ')

    def _get_sentence(self):
        if not self._degree and not self._starting_word:
            return
        a = time()
        trie = Trie(Node(), self._degree)
        trie.fill_with_words()

        mark = Markov(trie)
        sentence = mark.generate_sentence(self._starting_word, self._degree)
        b = time()
        if not sentence:
            sentence = 'Try another word or phrase'
        
        return sentence

    def _instructions(self):
        print('Commands:\n    h for help,\n    s to start,\n    other to exit.')
        return input('Command: ')
    
    def _help_page(self):
        print('\nplaceholder\n')
    
    def run(self):
        print('Welcome to the Markov chain text generator!\n')
        while True:
            next = self._instructions()
            if next == 'h':
                self._help_page()
            elif next == 's':
                self._start_process()
            else: return

            #print(b-a, 's')

    @staticmethod
    def main():
        ui = UI()
        ui.run()

