# Testing documentation

This project uses automated and end-to-end testing.

## Automated testing
Automated testing is done with the pytest library. The three main modules of the program, trie, markov_process and read_file, are tested this way.

Automated test coverage on Feb. 4. 2023

![test coverage](https://user-images.githubusercontent.com/94612974/216774955-ddb1bb55-972c-4fd7-aa2e-e3a327fbef8c.png)

### Trie and its nodes
The tests for the trie and node data structures help ensure that they work as intended. In their testing, the corpora used are very small, because the insertion of just one sentence into the trie should be adequate to tell whether the structure behaves as its excpected to.


### Markov
The tests for the Markov process are very basic and test only whether the process works with different inputs. The Markov process is 'stochastic' i.e. random, and randomness doesn't agree with unit tests. This module needs more tests.

The Markov process depends on the trie.


## End-to-end testing
I run my program with its numerous print statements and assess its output. The print statements lay out the execution of the Markov process, and the structure of the trie in use, and with repetitions I can confirm whether the program is working as intended. With this kind of testing, I can reassure the text generation is not deterministic and can find bugs and unintended behaviour.

The corpora used in e2e testing includes only full-sized books in Finnish and English. 
