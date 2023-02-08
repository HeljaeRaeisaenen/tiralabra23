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
A good trie works in linear time in the worst-case scenario. To test time complexity, I ran the program on two sizes of training material: Goethe's _Faust_ (345 707 bytes) and Victor Hugo's _Les Miserables_ (3 295 454 bytes). The larger is about 9.5 times the size of the smaller. If the trie of the program works in linear time, the difference is the execution speed should be roughly of the same scale.

I tested the program's execution time starting from the point where the file had already been read, and ending once the generated sentence had been printed. I ran seven trials with each training material.


|  | Faust | Les Miserables |
| - | ----- | -------------- | 
| time average |0.0905... | 1.72... | 

The ratio of the averages (time of Miserables / time of Faust) is ~19. If the program ran in linear time, one would expect the execution time with the larger material to be 9.5 times 0.0905 = ~0.86. This is about half of the attained speed, the attained speed is not exponential in relation to the size difference. This seems to be proof that the trie does work in linear time with some constant factor???

## Quality issues

## References
