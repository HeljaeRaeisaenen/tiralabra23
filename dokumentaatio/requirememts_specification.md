# Requirements Specification

## Purpose of the application
This application generates sentences that resemble natural language.

## About the project
This is a project of the Data Structures and Algorithms laboratory course (TKT kandi). The documentation and the project will be in English, but I can peer review in Finnish also.  

## Used Programming languages
This project is written in Python. I don't know any other language well enough to give peer reviews.

## The problem
The problem in making of this application is simulating natural language. The act of stringing together words into a sensible sentence requires some way to "understand" or model their relation to one another, which is implemented in the form of Markov chains: a simple way to predict which word could naturally follow the previous one.

To do this requires the manipulation of large amounts of words. A trie tree is well-suited for effective searches and mapping the relationships of words in a sentence.

It was recommended to use Markov chains and a trie in this project.

## Algorithms, data structures etc.
The application uses a trie tree and Markov chains, which I will implement myself.

### Markov chain
The Markov chain is a stochastic model.[1] In essence it describes the process of moving randomly from state to state, with the attained state being dependent on the previous state (or a number of previous states, _but not all_ of them). These transitions affect the probabilities of future transitions. 

### Trie
Trie is a tree structure.[2] Each node except the root has a value (a word in this case), and children. Usually when it comes to tries, each node is considered a letter of some alphabet or encoding. In this case, the alphabet consists of the words of a natural language (English or Finnish). These words are 'learned' from a corpus of training material. Moving down the tree creates a sequence of words. 

The children have probabilities attached, based on how often the child's value follows its parent's value in the training material. For example, "a red apple" is a fairly common phrase, wheareas "a red cucumber" is very rare. Picking the more common option is thought to create more meaningluf, or 'convincing-appearing' sentences. The transition from 'red' to 'cucumber' might not even be possible, if this hasn't happened in the training material. 

This is where a Markov chain process is involved. Each node is a state in a Markov chain. The next state can only be a child of the current state. Which of the children is picked is based on a weighted random choice which favours the more common children. What is more common is 'learned' from the training material.

## Time and space complexities
A well-made trie works in constant time, it's time complexity in a worst case scenario is O(n).[2] Thus the generation of a sentence should happen relatively efficiently.

However, a trie can be very inefficient when it comes to space. This is probably not a problem.

Determining which words are likely to follow each other demands a large amount of training data. Processing this data is likely a very time-consuming process. Storing the learned information on the computer in an easily accessible form would bypass the need to process the training data on each run.

## Functionality
The application will have a command-line, text-based user interface. A user can input a word, which will be the first word of the generated sentence. It is searched for among the children of the trie's root. If it isn't present in the training material, the user will be prompted to try another one. Otherwise a Markov process will then generate a sentence, which will be displayed to the user. 

Other functionality will likely be added.

## References
[1] https://en.wikipedia.org/wiki/Markov_chain
[2] https://en.wikipedia.org/wiki/Trie

