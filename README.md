# Tic-tac-toe-ML
Software that plays Tic-tac-toe by using machine learning
## How does the program work?
The software has a "rating" mechanism(Used to rank a board according to how good it is to the player who makes it and by that choice the next move) by calculating data on it and giving "weight" to each subject, the purpose of learning is to find the optimal weights

The learning / training process is done by 4 parts, when each part performs its function and transfers its output to the next part and repeats (sort of circle):
1. Experiment generator - This module create new "Experiment\Train"(random start board)
2. Performance system - This module play game against himself(When it uses the "ranking" of each move, it is possible to select the ideal move at each stage)
3. Critic - This module create train examples(pair of (board, ideal calculation of his rating)
4. Generalizer - Train using the training examples he got from the Critic
## How is the ranking mechanism processed?
The software calculates a long list of data and summarizes it while giving each one a certain "weight".
The data is list of 31 elements divided as follows:
* 0-8 - "1" if the corresponding place in the board is blank or "0" if not
* 9-17 - "1" if the corresponding place in the board is occupied by the player or "0" if not
* 18-26 - "1" if the corresponding place in the board is occupied by the other player or "0" if not
* 27 - If the player win in this board
* 28 - If the player lose in this board
* 29 - Player's chance of winning in the next turn (ranging from 0 to 1)
* 30 - Player's chance of losing in the next turn (ranging from 0 to 1)
## How he train himself?
To adjust the weights, the Generalizer uses a method called [LMS(Least mean squares filter)](https://en.wikipedia.org/wiki/Least_mean_squares_filter)