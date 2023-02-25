from pathlib import Path
from dotenv import dotenv_values
from constants import initialize, EmptyFileException
from trie import Node, Trie
from markov_process import Markov


class UI:
    '''Class for the UI and for orchestrating program execution.
    Attributes:
        _degree: The degree of the Markov chain to be used, given by user, int
        _starting_word: The word with which to start the generated sentence, given by user, str
        _default_file: Path to a file or folder, str
        _ansi_codes: A dict for storing ansi text modifying codes'''

    def __init__(self):
        self._degree = 2
        self._starting_word = ''
        try:
            self._default_file = dotenv_values('.env')['DEFAULT_FILEPATH']
        except KeyError:
            self._default_file = ''

        self._ansi_codes = {
            'red': "\u001b[31m",
            'bold': "\u001b[1m",
            'reset': "\u001b[0m"}

    def run(self):
        '''The backbone of the program, called when it's started.'''

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

    def _configure(self):
        '''Set the default filepath, and verify that it exists.'''

        file = input('Path or name of a file or folder: ')

        file = Path(file)

        if not file.exists():
            self._print_warning("The file or folder doesn't seem to exist.")
            return

        with open(".env", 'w', encoding='utf-8') as env:
            env.write(f"DEFAULT_FILEPATH={file}")
        self._default_file = str(file)

    def _start_generation_process(self):
        '''Initiate a state of the program, where the generation process is started.'''

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
        file = input('Give filename/path (\'e\' to exit): ')

        if file == 'e':
            return False

        if file and (not Path(file).exists()):
            file = self._default_file + '/' + file

        if not file:
            if not self._default_file:
                self._print_warning(
                    'Default file hasn\'t been set, please set it or input a filename/path.')
                return False
            file = self._default_file

        try:
            initialize(file)
            return True
        except (FileNotFoundError, EmptyFileException) as exception:
            self._handle_exception(exception, file)
            return False

    def _get_degree(self):
        degree = input('Give degree: ')
        if not degree:
            return
        try:
            self._degree = int(degree)
        except ValueError:
            self._print_warning("'Degree' must be a number (integer)")
            self._get_degree()

    def _get_word(self):
        try:
            self._starting_word = input('The sentence should start with: ')
        except UnicodeDecodeError:
            self._print_warning(
                'Processing the input caused a problem :C try again')
            self._get_word()

    def _get_amount(self):
        number = input('Number of sentences to generate: ')
        if not number:
            return 1

        try:
            number_validated = int(number)
            return number_validated
        except ValueError:
            self._print_warning(f'{number} is not a number (integer).')
            return self._get_amount()

    def _get_sentence(self):
        '''Initiate the actual Markov process and receive the generated sentence.
        Returns:
            sentence: if operation success, return a generated sentence (str), otherwise
            return False.'''

        trie = Trie(Node(), self._degree)
        trie.fill_with_words()

        if len(trie.root.give_children()) == 0:
            self._print_warning(
                '\nThere was an error, likely due to a too big degree value. Please try again.\n')
            return False

        mark = Markov(trie)
        sentence = mark.generate_sentence(self._starting_word, self._degree)
        if not sentence:
            print('\nTry another word or phrase.\n')
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

    def _handle_exception(self, exception, file):
        if isinstance(exception, FileNotFoundError):
            self._print_warning(
                f'\nCouldn\'t find a file called {file}, make sure that the file exists.\n')
        if isinstance(exception, EmptyFileException):
            self._print_warning(
                f'\nThe file/folder called {file} appears to not contain any acceptable text!\n')

    def _help_page(self):
        text = [
            "",
            "     - If you don't know what Markov chains are, read some of this:",
            "     https://en.wikipedia.org/wiki/Markov_chain",
            "     - When you press s and start the generation, you can give parameters.",
            "     - They're all optional if a default file/folder is set (read on).",
            "     - The path must be given as an absolute path, UNLESS the file is in the current",
            "     folder or the folder set as default",
            "     - The files must contain text that consists of sentences, e.g. prose or news.",
            "     - 'Degree' means how long 'chains' the program uses, a degree of 5 or less is",
            "     recommended.",
            "     - A higher degree risks that the program will just parrot the original text.",
            "     - You can also decide which word or phrase the generated sentences should start",
            "     or how many sentences you want.",
            "     - You can set a default file or folder in the c configurations. You should give",
            "     the ABSOLUTE path of the file/folder, including the file extension.",
            ""
        ]
        for line in text:
            print(line)

    @staticmethod
    def main():
        '''Allows the execution to be started neatly outside of the module. The class takes no
        params, so this is neat.'''
        ui_thing = UI()
        ui_thing.run()
