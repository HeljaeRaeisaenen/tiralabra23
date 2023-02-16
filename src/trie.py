import constants


class Node:
    '''Class for individual nodes of a trie
    Attributes:
        children: child nodes of the node
        value: the word associated with the node
        terminal: True if the node's word can end a sentence
        freq: the number of times this word appeared in its context in the source material'''

    def __init__(self, value=None, terminal=False):
        self.children = {}
        self.value = value
        self.terminal = terminal  # this isn't realöy needed
        self.freq = 0

    def give_children(self):
        '''Return the children of the node as a list'''
        return list(self.children.values())

    def __repr__(self):
        children = self.give_children()
        return f"\n{self.__class__}(children: {children}, value: {self.value}, freq.: {self.freq})"


############################################################################################


class Trie:
    '''Contains the methods needed for manipulating a trie.
    Attributes:
        root: root node of the trie
        degree: degree of the Markov chain that uses this trie'''

    def __init__(self, root, degree):
        self.root = root
        self.degree = degree

    def fill_with_words(self):
        '''Populate the trie with the source material. Adds rules of the Markov process to the
        trie. Makes testing easier to have an empty trie
        at first.'''
        for sentence in constants.SENTENCES:
            start_i = 0
            for i in range(self.degree+1, len(sentence)+1):
                part = sentence[start_i:i]
                self.insert(part)
                start_i += 1

    def insert(self, key):
        '''Insert a list of words into the trie
        Args:
            key: the list to be inserted'''
        node = self.root
        # print(key)
        for word in key:
            if word not in node.children.keys():
                # print(word, node.children[word])
                node.children[word] = Node(value=word)
                # print('added ',node.children[word])
            node = node.children[word]
            node.freq += 1
        # node.terminal = True
        # print('root ',self.root)

    def search(self, key: list):
        '''Search trie by a list of words.
        Args:
            key: a list of strings
        Returns:
            the children of the last word of the key, or False is key is not found'''
        node = self.root
        for word in key:
            if word not in node.children:
                # print('nope')
                return False
            node = node.children[word]
        return node.give_children()

    def __repr__(self) -> str:
        return str(self.root)
