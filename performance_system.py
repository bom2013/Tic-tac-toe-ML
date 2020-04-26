from experiment_generator import get_exp
from copy import deepcopy

# 0 - blank
# 1 - x
# 2 - o
# blank board = [[0,0,0],[0,0,0],[0,0,0]]
# all option = [[[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1]]]

# This function return the other player
def p_tag(player):
    if player == 1:
        return 2
    if player == 2:
        return 1
    return player

# This function print board in a slightly nicer shape
def print_board(b):
    print("-----")
    for i in range(len(b)):
        for j in range(len(b[i])):
            print(b[i][j], end=" ")
        print()
    print("-----")

# This function prints the entire course of the game
def print_game(m):
    for b in m:
        print_board(b)

# This function return all the legal move of player from specific board
def get_legal_moves(b, player):
    moves = []
    for i in range(9):
        if b[int(i/3)][i % 3] == 0:
            t_b = deepcopy(b)
            t_b[int(i/3)][i % 3] = player
            moves.append(t_b)
    return moves

#This function get "x" - the list of variable
def get_x(b, player):
    x = []
    for i in range(9):
        if b[int(i/3)][i % 3] == 0:
            x.append(1)
        else:
            x.append(0)
    for i in range(9):
        if b[int(i/3)][i % 3] == player:
            x.append(1)
        else:
            x.append(0)
    for i in range(9):
        if b[int(i/3)][i % 3] == p_tag(player):
            x.append(1)
        else:
            x.append(0)
    x.append(1 if is_end_of_game(b) == player else 0)
    x.append(1 if is_end_of_game(b) == p_tag(player) else 0)
    x.append(is_near_to_end(b, player))
    x.append(is_near_to_end(b, p_tag(player)))
    return x


#This function calculate the v(The ranking mechanism)
def calc_v(w, b, player):
    res = []
    x = get_x(b, player)
    for i in range(31):
        res.append(x[i]*w[i])
    return sum(res)


def is_near_to_end(b, player):
    m = get_legal_moves(b, player)
    if len(m) == 0:
        return (1 if is_end_of_game(b) == player else 0)
    w = 0
    for i in m:
        if is_end_of_game(i) == player:
            w += 1
    return w/len(m)

#This function check if the game end
#return:
#0 - The game is still happening
#1 or 2 - Victory to 1 or 2
#3 - draw
def is_end_of_game(b):
    for i in range(3):
        cx1 = 0
        co1 = 0
        cx2 = 0
        co2 = 0
        for j in range(3):
            if b[i][j] == 1:
                cx1 += 1
            if b[i][j] == 2:
                co1 += 1
            if b[j][i] == 1:
                cx2 += 1
            if b[j][i] == 2:
                co2 += 1
        if cx1 == 3:
            return 1
        if co1 == 3:
            return 2
        if cx2 == 3:
            return 1
        if co2 == 3:
            return 2
    if b[0][0] == 1 and b[1][1] == 1 and b[2][2] == 1:
        return 1
    if b[0][2] == 1 and b[1][1] == 1 and b[2][0] == 1:
        return 1
    if b[0][0] == 2 and b[1][1] == 2 and b[2][2] == 2:
        return 2
    if b[0][2] == 2 and b[1][1] == 2 and b[2][0] == 2:
        return 2
    for i in b:
        for j in i:
            if j == 0:
                return 0
    return 3

#This function return the best move from set of moves
def get_best_move(m, player, w):
    best_m = []
    v_arr = []
    for b in m:
        v_arr.append(calc_v(w, b, player))
    return m[v_arr.index(max(v_arr))]

# this function reverse the board(1<->2, 0<->0)
def reverse_board(b):
    r_b = []
    for i in b:
        t = []
        for j in i:
            t.append(p_tag(j))
        r_b.append(t)
    return r_b

# This function play game against himself
def play_game_against_himself(init_b, starter, w):
    cur_b = init_b
    cur_p = starter
    moves = [deepcopy(cur_b)]
    while is_end_of_game(cur_b) == 0:
        next_m = get_best_move(get_legal_moves(cur_b, cur_p), cur_p, w)
        cur_b = next_m
        moves.append(deepcopy(cur_b))
        cur_p = p_tag(cur_p)
    return moves

# This function play game against the user
def play_game_against_user(comp_p, w):
    cur_b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print_board(cur_b)
    while is_end_of_game(cur_b) == 0:
        next_m = get_best_move(get_legal_moves(cur_b, comp_p), comp_p, w)
        cur_b = next_m
        print_board(cur_b)
        x = int(input("enter x: "))
        y = int(input("enter y: "))
        cur_b[x][y] = p_tag(comp_p)
        print_board(cur_b)
    print("end, result: " + str(is_end_of_game(cur_b)))
