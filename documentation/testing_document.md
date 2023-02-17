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
The tests for the Markov process are very basic and test only whether the process works with different inputs. The Markov process is 'stochastic' i.e. random. The training material used in unit tests is mostly very small, to allow some control over what sentences can be generated.

Whether a generated sentence is possible to create with the set degree is also tested. The tests separate the generated sentence into 'rules' again, and check if those rules can be found in the Trie.

A Markov process shouldn't be determenistic, it shouldn't create the same sentence with the sane input, at least not every time. This is also tested for.

The Markov process depends on the trie, and if the trie works as intended, much of the validity of the Markov process is covered by that alone.

### Corpus processing tests
The program depends on one ugly function to parse a .txt-file into a usable form. This function, in the read_file module, called `split_into_sentences` is also tested. Its testing is mostly concerned with whether the processed sentences of the corpus are start and end at their actual starts and ends, whether periods inside sentences do not break a sentence, and whether punctuation marks are noticed and considered as their own 'words' (tokens).

## End-to-end testing
I run the program with numerous print statements and assess its output. The print statements lay out the execution of the Markov process, including the set of choices available at each step, and the structure of the trie in use, and with repetitions I can confirm whether the program is working as intended. With this kind of testing, I can reassure the text generation is not deterministic and can find bugs and unintended behaviour.

The corpora used in end-to-end testing consists of full-sized books in Finnish and English. I let the program randomly decide its starting word.

End-to-end testing can be replicated editing the source code to un-comment all commented print statements, and then running the program. 
