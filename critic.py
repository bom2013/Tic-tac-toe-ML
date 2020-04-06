import perf_sys


#train - [board, v_train, player]
def make_train_set(m, w, starter):
    train_list = []
    cur_p = starter
    game_res = perf_sys.is_end_of_game(m[-1]) #Should be either 1 or 2 or a draw (3)
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
            train_list.append([b, perf_sys.calc_v(w, m[m.index(b)+1], cur_p), cur_p])
        cur_p = perf_sys.p_tag(cur_p)
    return train_list

def player_after_n_moves(starter, n):
    if n%2 == 0:
        return starter
    return perf_sys.p_tag(starter)
