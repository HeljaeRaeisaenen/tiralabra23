# User instructions

## Get the program working


## On files
The program reads files and uses them to train itself to generate text. When running the program, the program prompts you to give a filename, file path or folder path. The program only accepts plaintext files (.txt).

In the configuration option, you can set a 'default file' for the program. This must be the full path to a file or to a folder. If you give a path to a folder, this is the default folder the program searches for files inputted by you, if you input only the filename + extension, and not a path. By default, this default path is the path to the folder named 'data' inside the project folder.

If the default path has been set, you can leave the filepath prompt empty by pressing enter.

If a path to a folder is given or configured and no filename is given, the program searches this folder for .txt files and reads them all. It's recommended to fill the folder with texts of only one language because:

1. The program cannot mix languages, so only the same language texts are used in the generation,

2. The program reads the files again every time, reading files takes time, and reading unusable files is a waste of time.

Note that the .txt files should contain natural language that consists of sentences. If the program can't find any sentences in the text, it gets confused and gives up!

## Degree
A Markov chain needs a parameter that is in some literature called a degree. This number signifies how long sequences of the source material it can parrot. A higher degree creates more real-looking text, but also means that the text is not very novel and might be entirely lifted from the source material. A degree of 1 means the process is almost random, and 0 creates text that is 0 words long.

A degree from 1 to 5 is probably optimal, but feel free to experiment.
