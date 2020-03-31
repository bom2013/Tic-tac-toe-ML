import perf_sys
def make_train_set(m, w, starter):
    train_list = []
    cur_p = starter
    for b in m:
        if b  == m[-1]:
            train_list.append([b, 100, cur_p])
        else:
            train_list.append([b, perf_sys.calc_v(w, m[m.index(b)+1], cur_p), cur_p])
        cur_p = perf_sys.p_tag(cur_p)
    return train_list

