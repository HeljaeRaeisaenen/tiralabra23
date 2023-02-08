# Implementation documentation
## Architecture
The program's logical structure is illustrated below.

```mermaid
classDiagram
  Trie-->Node
  MarkovProcess-->Trie
  UI-->MarkovProcess
  UI-->constants
  constants-->read_file
  MarkovProcess-->constants
  Trie-->constants
  Node-->constants

  class Node
    Node: dict children
    Node: str value
    Node: bool terminal
    Node: inst freq
    Node: give_children()
    
  class Trie
    Trie: Node root
    Trie: int degree
    Trie: fill_with_words()
    Trie: insert()
    Trie: search()
  
  class MarkovProcess
    MarkovProcess: Trie trie
    MarkovProcess: generate_sentence()
    MarkovProcess: calculate_weights()
    MarkovProcess: validate_starting_word()
    MarkovProcess: format_sentence()
    MarkovProcess: random_word()
    
  function read_file
  
  module constants
    constants: initialize()
    constants: set ALPHABET
    constants: list SENTENCES
  
    
  class UI
  ```

## Time complexity analysis
A good trie works in linear time in the worst-case scenario.

The program uses trie. The trie consists of nodes. The children of each node are in a lookup table of the node, so accessing them happens in constant time. The trie is created for the Markov process in index.py. There, it is given an empty node as its root. Next, the trie is populated with rules for the Markov process. The rules are lists of lenght degree+1, when degree is the degree of the Markov process. The trie's method `fill_with_words()` iterates through the corpus in a for-loop, which is a linear-time operation. The method has two nested for-loops, but the inner doesn't iterate the whole material, preserving the linear time complexity. This method uses another method of the trie, `insert()`. It searches the trie for each rule, which is relatively quick and doesn't affect the time complexity, as the rules are supposed to be degree+1 in length.

Next the program searches the trie an unknown amount of times. The search-method of the trie traverses the trie, accessing each node's children via the lookup table. This happens in linear time, as the search key is iterated through once.

All in all, the time complexity of the implemented trie should be O(n).

## Quality issues

## References
