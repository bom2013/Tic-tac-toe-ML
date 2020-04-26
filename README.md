# Tic-tac-toe-ML
Software that plays Tic-tac-toe by using machine learning

## How does the program work?
The software has a "rating" mechanism(Used to rank a board according to how good it is to the player who makes it and by that choice the next move) by calculating data on it and giving "weight" to each subject, the purpose of learning is to find the optimal weights

The learning / training process is done by 4 parts, when each part performs its function and transfers its output to the next part and repeats (sort of circle):
1. Experiment generator - This module create new "Experiment\Train"(random start board)
2. Performance system - This module play game against himself(When it uses the "ranking" of each move, it is possible to select the ideal move at each stage)
3. Critic - This module create train examples(pair of (board, ideal calculation of his rating)
4. Generalizer - Train using the training examples he got from the Critic
## How he train himself?
To adjust the weights, the Generalizer uses a method called [LMS(Least mean squares filter)](https://en.wikipedia.org/wiki/Least_mean_squares_filter)