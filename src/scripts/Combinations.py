import multiprocessing
import os

from .Data import *

# This function will divide the combinations between a number of processes
def distributeCombinations(listCombinations):
    processes = [None]*lengthPowers

    for i in range(0, lengthPowers):
        processes[i] = multiprocessing.Process(target=createCombination, args=(i, listCombinations))
        processes[i].start()

    for i in range(0, lengthPowers):
        processes[i].join()

# This function will create a limited number of combinations
def createCombination(powerPosition, listCombinations):
    possibleCombinations = pow(lengthPowers, lengthConstants)/lengthPowers
    repeatOperation = False
    i = possibleCombinations*powerPosition

    print("Process", powerPosition, "started")

    while (i < possibleCombinations*(powerPosition + 1)):
        combination = ""
        solution = 1
        units = 1

        for j in range(0, lengthConstants):
            constant = constants[0][j][0]
            power = powers[int((i/(pow(lengthPowers, lengthConstants - j)/lengthPowers))%lengthPowers)];
            solution *= constant**power
            units *= constants[0][j][1]**power

            if (repeatOperation == True):
                combination += str(constant) + "^" + str(power)

                if (j < (lengthConstants - 1)):
                    combination += " * "

        if (units - constants[1][1] == 0):
            if (repeatOperation == True):
                listCombinations.append([combination, solution])
                repeatOperation = False
            else:
                repeatOperation = True;
                i -= 1

        i += 1

    print("Process", powerPosition, "finished")