# Testing documentation

This project uses automated and end-to-end testing.

## Automated testing
Automated testing is done with the pytest library. The three main modules of the program, trie, markov_process and read_file, are tested this way.

![test coverage](https://user-images.githubusercontent.com/94612974/216774955-ddb1bb55-972c-4fd7-aa2e-e3a327fbef8c.png)

The tests can be replicated by running `poetry run invoke test` in the repository's root folder. The tests are also ran each time a commit is added or pushed on the GitHub page.

### Trie and its nodes
The tests for the trie and node data structures are concerned whether the trie has the intended structure. In their testing, the corpora used are very small, because the insertion of just one sentence into the trie should be adequate to tell whether the structure behaves as its excpected to.

The tests test whether an added sentence can be found in the trie, and if the relationships between its words is correct.

### Markov
The tests for the Markov process are very basic and test only whether the process works with different inputs. The Markov process is 'stochastic' i.e. random, and randomness doesn't agree with unit tests. This module needs more tests.

The Markov process depends on the trie.


## End-to-end testing
I run my program with numerous print statements and assess its output. The print statements lay out the execution of the Markov process, including the set of choices available at each step, and the structure of the trie in use, and with repetitions I can confirm whether the program is working as intended. With this kind of testing, I can reassure the text generation is not deterministic and can find bugs and unintended behaviour.

The corpora used in end-to-end testing includes only full-sized books in Finnish and English. I let the program randomly decide its starting word.

End-to-end testing can be replicated editing the source code to un-comment all commented print statements, and then running the program. 
