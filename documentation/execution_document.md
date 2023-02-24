# Execution documentation
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

Analysis:

The program uses trie. The trie consists of nodes. The children of each node are in a lookup table of the node, so accessing them happens in constant time. The trie is created for the Markov process in index.py. There, it is given an empty node as its root. Next, the trie is populated with rules for the Markov process. The rules are lists of lenght degree+1, when degree is the degree of the Markov process. The trie's method `fill_with_words()` iterates through the corpus in a for-loop, which is a linear-time operation. The method has two nested for-loops, but the inner doesn't iterate the whole material, preserving the linear time complexity. This method uses another method of the trie, `insert()`. It searches the trie for each rule, which is relatively quick and doesn't affect the time complexity, as the rules are supposed to be degree+1 in length.

Next the program searches the trie an unknown amount of times. The search-method of the trie traverses the trie, accessing each node's children via the lookup table. This happens in linear time, as the search key is iterated through once.

All in all, the time complexity of the implemented trie should be O(n).

## Corpus
I've built this program using txt-format e-books as its corpora. Books like this can easily be found on the websites of Project Gutenberg and Projekti Lönnrot. Any plain text file should be good to use with this program, but note that the program isn't prepared to parse URLs and that some types of texts with might behave funny.

## Quality issues

### Quotation mark control
In class Markov, there is a bunch of code that attempts to force the process to close opened quotes, and not close unopened quotes, to try and avoid text like:

'I like puppies" he said.'

If you look at the class' method generate_sentence(), you can see that there's a loop that iterates with range:

```
for i in range(len(next_words)):
      chosen_one = choices(next_words, cum_weights=weights, k=1)[0]
                
          if chosen_one.value == '“':
		...
```
The iteration exist to get allow the insertion of an unwanted quote mark in the sentence, if it is the only currently available candidate for the next 'word' (or token). The range gives the code as many tries as there are these candidates to take a weighted random choice. If the first choice is an unwanted quote mark, a new choice is made, until the code either finds a more suitable next word, or  "gives up".

This improves the quality of the generated text a little bit, but is ugly.

### Deviation from a textbook trie
A trie's nodes usually have a terminal value, that tell whether they can end a sequence. In my program, periods, exclamation marks etc. are considered words which can be stochastically chosen in the Markov process, and these never have children. Instead of having a terminal value, ending nodes just don't have any children, thus terminating the sequence.

A proper trie contains a dictionary, lookup table etc. of its children, and this dictionary has keys for all the symbols of the alphabet used. If a certain symbol can't follow the current one, its dictionary key refers to a void value. However, when the alphabet is a large subset of all words in a natural language, creating these dicts is very time-consuming, so I decided to include only existent children in the dict.

I also added the nodes an attribute named value, which is the node's symbol. The value should be implicit in the node's position inside the trie, so this is a bit of a lazy approach.

### Long execution time
If the corpus is large, e.g. contains several novels, the program's excecution takes several seconds. 

## References
https://en.wikipedia.org/wiki/Markov_chain
https://en.wikipedia.org/wiki/Trie
https://bespoyasov.me/blog/text-generation-with-markov-chains/
