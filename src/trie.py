'''With help from the pseudocode at https://en.wikipedia.org/wiki/Trie'''
from index import ALPHABET, sentences


class Node:
    '''Class for individual nodes of a trie
    Attributes:
        children: child nodes of the node
        value: the word associated with the node
        terminal: True if the node's word can end a sentence'''

    def __init__(self, value=None, terminal=False):
        self.children = {}
        self.value = value
        self.terminal = terminal

        for word in ALPHABET:
            self.__add_alphabet_key(word)

    def __add_alphabet_key(self, child):
        '''Ensure all members of the alphabet are already as keys for the node's children'''
        self.children[child] = None

    def give_children(self):
        '''Return children that are nodes, not Nones'''
        children = []
        for key, child in self.children.items():
            if child:
                children.append(child)
    
        return children


    def __repr__(self):
        children = self.give_children()

        return f"\n{self.__class__}(children: {children}, value: {self.value}, {self.terminal})"


############################################################################################


class Trie:
    '''Constains the methods needed for manipulating a trie.
    Attributes:
        root: root node of the trie'''

    def __init__(self, root, sentences):
        self.root = root
        self.lookup = {}

        for word in ALPHABET:
            self.lookup[word] = set()
        for sentence in sentences:
            self.insert(sentence)

    def insert(self, key):
        '''Insert a whole sentence into the trie'''
        # print(key)
        node = self.root
        # print(node is self.root)

        for word in key:
            if not node.children[word]:
                # print(word, node.children[word])
                node.children[word] = Node(value=word)
                # print('added ',node.children[word])
            node = node.children[word]
            self.lookup[node.value].add(node)
        node.terminal = True
        # print('root ',self.root)
    
    def search(self, key:list):
        '''Search trie by a list of words.
        Args:
            key: a list of strings
        Returns:
            the node corresponding to the key in the trie'''
        node = self.root
        for word in key:
            if not node.children[word]:
                return False
            node = node.children[word]
        return node

    def search_hack(self, key):
        '''Searching through the whole trie is time consuming, hence lookup table'''
        return self.lookup[key]

    def __repr__(self) -> str:
        return str(self.root)


if __name__ == '__main__':
    rootnode = Node()
    # print(rootnode)
    trie = Trie(rootnode, sentences)
    print(trie)
