# Week report
Week 2

Hours: 14

## What did I do?
This week I made a trie and began working on the Markov process of the program. 

## How did I progress?
The program is now able to create random sentences that follow the 'rules' defined by the trie: a given word can only be followed by words that follow said word in the training material. Which of the possible words is selected is random. I think the trie is pretty much finished, and what's left is to make the Markov process work.

My program also terribly slow just a while ago, taking several seconds to finish. This was because I followed the trie feature, that each node should have a table of all the symbols of the alphabet as its children, with only some of them in use by actual children. This ensured no key errors happen, but the alphabet of a whole book is enormous, and the program iterated through it when creating every node. I got rid of this feature.

## What did I learn?
I learned how much a little change can speed up a program.

## Problems
The search-methods of a general trie that are laid out on wikipedia and other sites seem to only be able for finding words (/sentences) that do appear in the source material. The methods are used to determine wether a given string "belongs to the language" of the trie. The first character (/word) of the search key is searched for only in the set of all the characters that have started a word in the source material, and the search continues on this branch of the trie. Now I know why it's called a 'prefix tree'. This isn't really helpful here, as the goal is to generate novel sentences. I'm working on modifying the search method so that it'll allow matching also substrings everywhere in the trie, not only a specific string.

## What next?
Next I will make the actual Markov process with weighted random choices, and before that, the search method.
