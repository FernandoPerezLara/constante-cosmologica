#!/usr/bin/env python

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
    
    properties = readArguments()

    if (properties.parameters == True):
        print("Number of constants:", lengthConstants)
        print("Number of powers:", lengthPowers)

    time[0] = datetime.now()
    print("\nStart time:", str(int(time[0].timestamp())))

    distributeCombinations(listCombinations)
    combinations = list(listCombinations)
    combinations.sort(key=lambda x: x[1] - constants[1][0])

    time[1] = datetime.now()
    print("Ending time:", str(int(time[1].timestamp())), "\n")
    print("Number of combinations:", len(combinations))

    if (properties.dontSave == False):
        saveCombinations(combinations, time)

    if (properties.hide == False):
        if (len(combinations) != 0):
            print("\nResults [combinations = solution | (solution - cosmological constant)]:")
            for i in range(0, len(combinations)):
                print(combinations[i][0], "=", combinations[i][1], "|", combinations[i][1] - constants[1][0])
        else:
            print("\nWithout results")

# This function exports the output in a ".txt" file
def saveCombinations(combinations, time):
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/data"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file = open(dir_path + "/" + str(int(time[1].timestamp())) + ".txt", "w")
    
    file.write("Start time: " + str(int(time[0].timestamp())) + "\n")
    file.write("Ending time: " + str(int(time[1].timestamp())) + "\n")

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
        file.write("\nResults [combinations = solution | (solution - cosmological constant)]:\n")
        for i in range(0, len(combinations)):
            file.write("\t" + str(combinations[i][0]) + " = " + str(combinations[i][1]) + " | " + str(combinations[i][1] - constants[1][0]) + "\n")
    else:
        file.write("\nWithout results")

if __name__ == "__main__":
    main()