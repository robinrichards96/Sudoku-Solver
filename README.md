# Sudoku-Solver
This repository contains an algorithm written in Python that solves any 9x9 Sudoku

I am an avid Sudoku solver myself so I was interested in how easy it would be to automate this task in Python. During my research on this topic I found that the backtracking algorithm was the most favoured among other people who had created something similar.
While there are several other ways to do this, such as with the Naive algorithm, constraint propogation or search. However, backtracking provided the most concise and elegant solution to this problem.

I found that of all the existing solutions that I looked at, techwithtim has created the simplest and most elegant code. This is what I used for inspiration for my solution, which uses 3 functions: one to check whether the square in the Sudoku is empty (and requires filling), one to check whether the number is valid (i.e. does it satisfy the rules of Sudoku), and one to actually fill in the numbers and use the backtracking algorithm if it spots a break in the rules.
