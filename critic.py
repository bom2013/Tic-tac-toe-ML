'''
This module create train examples from game
'''
import performance_system


#train - [board, v_train, player]
#This function create train set(set of train examples)
def make_train_set(m, w, starter):
    train_list = []
    cur_p = starter
    game_res = performance_system.is_end_of_game(m[-1]) #Should be either 1 or 2 or a draw (3)
    for b in m:
        if b == m[-2]:#he lose\draw, cant win
            if game_res == 3:#draw
                train_list.append([b, 0, cur_p])
            else: #he lose
                train_list.append([b, -100, cur_p])
        elif b  == m[-1]:#he win\draw
            if game_res == 3:#draw
                train_list.append([b, 0, cur_p])
            else:
                train_list.append([b, 100, cur_p])
        else:
            train_list.append([b, performance_system.calc_v(w, m[m.index(b)+1], cur_p), cur_p])
        cur_p = performance_system.p_tag(cur_p)
    return train_list

#This function return who is the player after n moves from start
def player_after_n_moves(starter, n):
    if n%2 == 0:
        return starter
    return performance_system.p_tag(starter)
