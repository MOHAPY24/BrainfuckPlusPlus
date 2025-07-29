# TIRLL++
## An extremely lightweight, low-level remastered version of the BF Esolang.

## What is TIRL++?
TIRL++ (Tape Based Interperted Remastered Low-level Lightweight-language)  is a low level lightweight esolang based on BF, ran based on a 110-130 line python interperter

## How to run TIRLL++?
Download the interperter and make a file with a .bfpp or .bfa file extension at the end and start coding
the basic syntax are

">" - move the pointer to the next cell

"<" - move the pointer to the cell before it

"+" - add to the current cell

"-" - remove from the current cell

"." - print current cell

"," - end file (needed at EOF or else syntax error will be raised)

"@" - print entire tape then make all cells in tape = 0

"$" - start comment

"/" - end comment

"*" - multiply the current cell by itself

" ' " - take current cell contants and put into cell 0, also puts pointer back to cell 0

"#" - Take the contants of the cell before the current cell into the current cell

"|" - saves current cell contants

"%" - loads saved cell contants in current cell

More updates soon!


