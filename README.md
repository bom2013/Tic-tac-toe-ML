# Tic-tac-toe-ML
Software that plays Tic-tac-toe by using machine learning
## How to use this program?
First run the manager.py, you will have all what you need in the main menu
## How does the program work?
The software has a "rating" mechanism(Used to rank a board according to how good it is to the player who makes it and by that choice the next move) by calculating data on it and giving "weight" to each subject, the purpose of learning is to find the optimal weights.

The learning / training process is done by 4 parts, when each part performs its function and transfers its output to the next part and repeats (sort of circle):
1. Experiment generator - This module create new "Experiment\Train"(random start board)
2. Performance system - This module play game against himself(When it uses the "ranking" of each move, it is possible to select the ideal move at each stage)
3. Critic - This module create train examples(pair of (board, ideal calculation of his rating)
4. Generalizer - Train using the training examples he got from the Critic
## How is the ranking mechanism processed?
The software calculates a long list of data and summarizes it while giving each one a certain "weight".
The data is list of 31 elements that include:
* which places in the board empty
* which places in the board is occupied by the player
* which places in the board is occupied by the other player
* If the player win\lose in this board
* Player's chance of winning\losing in the next turn
## How he train himself?
To adjust the weights, the Generalizer uses a method called [LMS(Least mean squares filter)](https://en.wikipedia.org/wiki/Least_mean_squares_filter)
## Thoughts and wonder
I built this project out of interest if it works, the whole mechanism is pretty primitive, it's actually a "neuron network" with only one neuron ...  
In addition, the vector is very small (a total of 31 things to consider in the calculation), so I did not expect any improvement as a result of the learning process.  
In the end, after running 250,000 workouts, there was some improvement, not enough to beat a person, but you can definitely see that he's not "guessing".
I suppose if you improve the amount of things it takes in his calculation(the vector) the software will work better.
## Development
As I mentioned before, this was only develop as an experiment, but if you have any comments, please feel free to contact me / send a PR