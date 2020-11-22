#!/usr/bin/env python

from itertools import combinations
import os
from datetime import datetime
import multiprocessing

from scripts import *

# Initializer function
def main():
    manager = multiprocessing.Manager()
    listCombinations = manager.list()
    combinations = []
    time = [datetime.now(), datetime.now()]

    os.system("clear");

    time[0] = datetime.now()
    print("Start time:", time[0].strftime("%H:%M:%S"))

    distributeCombinations(listCombinations)
    combinations = list(listCombinations)
    combinations.sort(key=lambda x: x[1] - constants[1][0])

    time[1] = datetime.now()
    print("Ending time:", datetime.now().strftime("%H:%M:%S"))
    print("Number of combinations:", len(combinations))

    saveCombinations(combinations, time)

# This function exports the output in a ".txt" file
def saveCombinations(combinations, time):
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/data"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file = open(dir_path + "/" + str(int(time[1].timestamp())) + ".txt", "w")
    
    file.write("Start time: " + time[0].strftime("%H:%M:%S") + "\n")
    file.write("Ending time: " + time[1].strftime("%H:%M:%S") + "\n")

    file.write("\nCosmological constant: " + str(constants[1][0]) + " " + str(constants[1][1]) + "\n");

    file.write("\nConstants:\n")
    for i in range(0, lengthConstants):
        file.write("\t" + str(constants[0][i][0]) + " " + str(constants[0][i][1]) + "\n")

    file.write("\nPowers: ")
    for i in range(0, lengthPowers - 1):
        file.write(str(powers[i]) + ", ")
    file.write(str(powers[lengthPowers - 1]) + "\n")

    file.write("\nNumber of combinations: " + str(len(combinations)) + "\n")

    if (len(combinations) != 0):
        print("\nResults [combinations = solution | (solution - cosmological constant)]:")
        file.write("\nResults [combinations = solution | (solution - cosmological constant)]:\n")
        for i in range(0, len(combinations)):
            print(combinations[i][0], "=", combinations[i][1], "|", combinations[i][1] - constants[1][0])
            file.write("\t" + str(combinations[i][0]) + " = " + str(combinations[i][1]) + " | " + str(combinations[i][1] - constants[1][0]) + "\n")
    else:
        print("\nWithout results")
        file.write("\nWithout results")

if __name__ == "__main__":
    main()