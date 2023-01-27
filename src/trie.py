import constants


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
        self.freq = 0

    def give_children(self):
        '''Return children of the node as a list'''
        children = []
        for child in self.children.values():
            children.append(child)

        return children

    def __repr__(self):
        children = self.give_children()

        return f"\n{self.__class__}(children: {children}, value: {self.value}, freq.: {self.freq})"


############################################################################################


class Trie:
    '''Contains the methods needed for manipulating a trie.
    Attributes:
        root: root node of the trie'''

    def __init__(self, root):
        self.root = root
        self.lookup = {}

        for word in constants.ALPHABET:
            self.lookup[word] = set()

    def fill_with_sentences(self):
        '''Makes testing easier to have an empty trie at first.'''
        for sentence in constants.SENTENCES:
            self.insert(sentence)

    def insert(self, key):
        '''Insert a whole sentence into the trie'''
        # print(key)
        node = self.root

        for word in key:
            if word not in node.children.keys():
                # print(word, node.children[word])
                node.children[word] = Node(value=word)
                # print('added ',node.children[word])
            node = node.children[word]
            node.freq += 1
            self.lookup[node.value].add(node)
        node.terminal = True
        # print('root ',self.root)

    def search(self, key: list):
        '''Search trie by a list of words. Only nodes whose parental sequence matches the key.
        Args:
            key: a list of strings
        Returns:
            list containing all hits'''
        result = []
        nodes = self.search_quick(key[0])
        # node = self.root
        for node in nodes:
            for word in key[1:]:
                print('searching ', word, 'in', node.value)
                if word not in node.children.keys():
                    print('not found')
                    break
                node = node.children[word]
                print('found ', node.value)
            result += node.give_children()
            print('added to result ', node.value)
        return result

    def search_quick(self, key):
        '''Searching through the whole trie is time consuming, so lookup table'''
        return self.lookup[key]

    def __repr__(self) -> str:
        return str(self.root)


if __name__ == '__main__':
    constants.init('tests/testdata/catsanddogs.txt')
    rootnode = Node()
    trie = Trie(rootnode)
    trie.fill_with_sentences()
    print(trie)
