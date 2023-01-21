# Week report
Week 1

Hours: 

## What did I do?
This week I mainly tried to understand how Markov chains work, or what they even are. I began planning how to construct this app, or how it's supposed to work on a fundamental level.

I spent most of the time reading about tries and Markov chains, watching some videos, and drawing/writing sketches to help me understand them. I currently have a quite solid understanding of what I need to do, and can start writing code next week.

I began planning which which "corpus" to use for training my program. As I don't want to spend time reading about copyright laws, I decided to use copyright-free training material. Project Gutenberg has copious amounts of digital books that are in the public domain in the USA. 'Projekti Lönnrot' has copyright-free books in Finnish.

## How did I progress?
I made a plan for how I will write this program. I learned a lot and have a basic understanding of the data structrures and model I'll use. I began gathering and processing training material for the model and writing a module for this task. My program can currently split a wall of text into sentences and words, yay :p

## What did I learn?
I learned what a trie is. A trie is a tree that is efficient for searching sequences of characters. It's supposedly used in some types of autocorrect and autocomplete solutions, and so it makes sense that it'll be helpful in text generation.

I learned what a 'stochastic model' is and what Markov chains are.

## Problems
I'm not sure if I understood what a trie or markov chain are _correctly_. If there is a 'one true way' to make this program, I'm not so sure I get it.

I also couldn't figure out how to make pytest find the files in the tests/testdata folder. One fix I found was to run pytest inside the src folder, but because of this coverage needs to also be run inside the src folder.

## What next?
Next I will begin writing a trie, and hopefully make a working skeleton of the program.
