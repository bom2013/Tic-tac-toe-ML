import perf_sys
from copy import deepcopy

#get_x(b, player)
#calc_v(w, b, player)
#1 train = [b, v_train, p]
def LMS_update(train_set, w):
    cur_w = deepcopy(w)
    for t in train_set:
        cur_b = t[0]
        cur_v_train = t[1]
        cur_p = t[2]
        new_w = []
        v_old = perf_sys.calc_v(cur_w, cur_b, cur_p)
        cur_x = perf_sys.get_x(cur_b, cur_p)
        for i in cur_w:
            x_i = cur_x[cur_w.index(i)]
            new_w.append(i+0.01 * (cur_v_train - v_old) * x_i)
        cur_w = new_w
    return cur_w

    
