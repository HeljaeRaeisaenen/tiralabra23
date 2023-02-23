from pathlib import Path
from constants import initialize
from trie import Node, Trie
from markov_process import Markov
from dotenv import dotenv_values


class UI:
    def __init__(self) -> None:
        self._degree = None
        self._starting_word = None
        try:
            self._default_file = dotenv_values('.env')['DEFAULT_FILEPATH']
        except KeyError:
            self._default_file = None

        self._ansi_codes = {
            'red': "\u001b[31m",
            'bold': "\u001b[1m",
            'reset': "\u001b[0m"}

    def run(self):
        print('\nWelcome to the Markov chain text generator!\n')
        while True:
            command = self._instructions()
            if command == 'h':
                self._help_page()
            elif command == 'c':
                self._configure()
            elif command == 's':
                self._start_generation_process()
            else:
                return

            # print(b-a, 's')

    def _configure(self):
        file = input('Path or name of the file: ')
        with open(".env", 'w', encoding='utf-8') as env:
            env.write(f"DEFAULT_FILEPATH={file}")
        self._default_file = file

    def _start_generation_process(self):
        while True:
            success = self._open_file()
            if not success:
                return
            self._get_degree()
            self._get_word()
            amount = self._get_amount()
            for i in range(amount):
                result = self._get_sentence()
                if not result:
                    break
                print('\n'+result+'\n')

    def _open_file(self):
        path = 'data/'
        file = input('Give filename/path (\'e\' to exit): ')
        if file == 'e':
            return False
        if not file:
            if not self._default_file:
                self._print_warning(
                    'Default file hasn\'t been set, please set it or input a filename.')
                return False
            file = Path(self._default_file).resolve()
            print('     Generating from: ', file)
        else:
            if file[-4:] != '.txt':
                file += '.txt'

            if 'src' in str(Path('.').resolve()):
                path = '../data/'

            if not 'home' in file:
                file = Path(path+file).resolve()

        try:
            initialize(file)
            return True
        except FileNotFoundError:
            self._print_warning(
                f'\nCouldn\'t find a file called {file}, make sure that the file exists.\n')
            return False

    def _get_degree(self):
        degree = input('Give degree: ')
        if not degree:
            degree = 2
        try:
            self._degree = int(degree)
        except ValueError:
            self._degree = 2
            self._print_warning("'Degree' must be a number")
            return

    def _get_word(self):
        self._starting_word = input('The sentence should start with: ')

    def _get_amount(self):
        number = input('Number of sentences to generate: ')
        if not number:
            return 1

        try:
            number_validated = int(number)
            return number_validated
        except ValueError:
            self._print_warning(f'{number} is not a number.')
            return 1

    def _get_sentence(self):
        if not self._degree and not self._starting_word:
            return
        trie = Trie(Node(), self._degree)
        trie.fill_with_words()

        mark = Markov(trie)
        sentence = mark.generate_sentence(self._starting_word, self._degree)
        if not sentence:
            print('\nTry another word or phrase\n')
            return False

        sentence = self._ansi_wrap(sentence, 'bold')
        return sentence

    def _instructions(self):
        print(
            'Commands:\n    h for help,\n    s to start,\n    c to configure,\n    other to exit.')
        return input('Command: ')

    def _ansi_wrap(self, text, code):
        return self._ansi_codes[code] + text + self._ansi_codes['reset']

    def _print_warning(self, text):
        text = self._ansi_wrap(text, 'red')
        print(text)

    def _help_page(self):
        text = [
            "",
            "     - If you don't know what Markov chains are, read some of this:",
            "     https://en.wikipedia.org/wiki/Markov_chain",
            "     - When you press s and start the generation, you can give parameters.",
            "     - They're all optional if a default file is set (read on).",
            "     - The file must be given as an absolute path, UNLESS the file is in the 'data'",
            "     folder (see user instructions: [link])."
            "     - 'Degree' means how long 'chains' the program uses, a degree of 5 or less is",
            "     recommended.",
            "     - A higher degree risks that the program will just parrot the original text.",
            "     - You can also decide which word or phrase the generated sentences should start",
            "     or how many sentences you want.",
            "     - You can set a default file in the c configurations. You should give the",
            "     ABSOLUTE path of the file, including the filename and extension."
            ""
        ]
        for line in text:
            print(line)

    @staticmethod
    def main():
        ui_thing = UI()
        ui_thing.run()
