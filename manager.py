import critic
import perf_sys
import exp_gen
import generalizer
from random import uniform
#w = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#print(critic.make_train_set(perf_sys.play_game_against_himself([[0,0,0],[0,0,0],[0,0,0]], 1, w), w, 1))

NUM_OF_TEST =250000
w=[]
for i in range(31):
    w.append(uniform(-5.0, 5.0))
print(w)
with open("w_start.txt", "w")as f:
    f.write(str(w))
for i in range(NUM_OF_TEST):
    s_b = exp_gen.get_exp(1)
    m = perf_sys.play_game_against_himself(s_b, 2, w)
    ts = critic.make_train_set(m, w, 1)
    w = generalizer.LMS_update(ts, w)
    if i%100 == 0:
        print("do: "+ str(100*(i/NUM_OF_TEST)) + "%")
print("Done!")
print(w)
#input("enter to play against comp")
#perf_sys.play_game_against_user(1,w)
with open("w_learned.txt", "w")as f:
    f.write(str(w))
