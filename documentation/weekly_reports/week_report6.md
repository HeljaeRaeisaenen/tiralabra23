# Week report
Week 6

Hours: 12

## What did I do?
This week I proofed the program against errors, and added the possibility to use several files as the corpus. I also end-to-end tested the program a lot and made many small improvements.

## How did I progress?
The program is now more enjoyable to use and the code looks prettier. The test coverage is a bit higher too.

## What did I learn?
I learned to use python's pathlib module.

## Problems
I found out that when using python input, the letter 'ä' behaves in a weird way. When you write one 'ä', nothing shows in the terminal, but when you write another letter 'ä', 'ää' becomes visible. If you write two 'ä's in a row and then erase one of them, python doesn't recognize the text as 'utf-8' coded, and if you erase all text, you can also erase some of the UI text! This bug exists becasue 'ä' is 2 bytes long, while python doesn't expect letters that long, I think? I don't know if I'll fix this bug and I can't replicate it outside of my program.

## What next?
Next is just polishing.
