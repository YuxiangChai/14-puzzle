# 14 Puzzle

### Introduction

- In a 4x4 board, there are two blanks and 14 tiles numbered from 1 to 14. Each
  tile can move up, down, left or right in one step if a blank is adjacent.

- Given a .txt file which includes initial state and goal state, output a .txt
  file including *initial state*, *goal state*, *number of steps*, *number of
nodes*, *steps in detail* and *result of evaluation function*.

- In this case, A\* search strategy is used and *sum of Manhattan distances of
  tiles from their goal positions* is used as heuristic function.


### How to run the program
- Put an input file in the same folder and name it _'Input\*.txt'_.

- Open a new terminal window and type in the following command:
```python
python3 14_puzzle.py Input*.txt
```

- A new ouput file _'Output\*.txt'_ will be created in the folder.
