import multiprocessing

from .Data import *

# This function will divide the combinations between a number of processes
def distributeCombinations(listCombinations):
    processes = [None]*lengthPowers

    # Create the processes required to create the joins
    for i in range(0, lengthPowers):
        processes[i] = multiprocessing.Process(target=createCombination, args=(i, listCombinations))
        processes[i].start() # Begins the process

    # Wait for all the processes to complete
    for i in range(0, lengthPowers):
        processes[i].join() # Wait the process

# This function will create a limited number of combinations
def createCombination(powerPosition, listCombinations):
    possibleCombinations = pow(lengthPowers, lengthConstants)/lengthPowers
    repeatOperation = False
    i = possibleCombinations*powerPosition

    # Generates a group of combinations
    while (i < possibleCombinations*(powerPosition + 1)):
        combination = ""
        solution = 1
        units = 1

        # Generate a single combination
        for j in range(0, lengthConstants):
            power = powers[int((i/(pow(lengthPowers, lengthConstants - j)/lengthPowers))%lengthPowers)];
            units *= pow(constants[0][j][1], power)

            # Save the combination
            if (repeatOperation == True):
                constant = constants[0][j][0]
                solution *= pow(constant, power)
                combination += str(constant) + "^" + str(power)

                if (j < (lengthConstants - 1)):
                    combination += " * "

        # This combination has to be saved
        if (units - constants[1][1] == 0):
            if (repeatOperation == True):
                listCombinations.append([combination, solution])
                repeatOperation = False
            else:
                repeatOperation = True;
                i -= 1

        i += 1