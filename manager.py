import critic
import performance_system
import experiment_generator
import generalizer
from random import uniform

'''
This module used for train management and study with the other modules
'''
end_main = False
while not end_main:
    print("--------------")
    print("Welcome to manager view")
    print("1. Create and train new weight")
    print("2. Play game using weight")
    print("3. Exit")
    inp = int(input('Enter your choice: '))
    if inp == 1:
        num_of_trains = int(input('Enter number of trains: '))
        print("Creates a starting vector with random values")
        w = []
        for i in range(31):
            w.append(uniform(-5.0, 5.0))
        print("Starting vector is: ")
        print(w)
        if input("Do you want to save start vector in file before running the learning process(y\\n)? ") == "y":
            with open(input("Enter file name: ")+".txt", "w")as f:
                f.write(str(w))
            print("File saved")
        print("Start lerning process")
        for i in range(num_of_trains):
            s_b = experiment_generator.get_exp(1)
            m = performance_system.play_game_against_himself(s_b, 2, w)
            ts = critic.make_train_set(m, w, 1)
            w = generalizer.LMS_update(ts, w)
            if i % 100 == 0:
                print("update: " + str(100*(i/num_of_trains)) + "%")
        print("Done!")
        print(w)
        if input("Do you want to save the vector(y\n)? ") == "y":
            with open(input("Enter file name: ")+".txt", "w")as f:
                f.write(str(w))
            print("File saved")
        print("Finish training, return to main menu")
    elif inp == 2:
        w = []
        with open(input("Enter file name: ")+".txt", "r")as f:
            w = list(f.read())
        print("Weight loaded")
        print("Start game, have fun!")
        performance_system.play_game_against_user(1, w)
        print("Finish game, return to main menu")
    else:
        exit()
