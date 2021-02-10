import multiprocessing
import sympy as sym

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
    possibleCombinations = (lengthPowers**lengthConstants)/lengthPowers
    subgroup = possibleCombinations*(powerPosition + 1)
    repeatOperation = False
    ignoreSolution = False
    i = possibleCombinations*powerPosition

    # Made to remove the square roots of the powers
    constants[1][1] = constants[1][1]**2

    # Generates a group of combinations
    while (i < subgroup):
        combination = ""
        solution = 1
        units = 1

        # Generate a single combination
        for j in range(0, lengthConstants):
            power = sym.Rational(powers[int(i*(lengthPowers**(1 - lengthConstants + j)) % lengthPowers)])
            units *= constants[0][j][1]**power

            # Save the combination
            if (repeatOperation == True):
                constant = constants[0][j][0]
                combination += str(constant) + "^" + str(power)

                if (ignoreSolution == False):
                    try:
                        solution *= constant**power
                    except OverflowError:
                        solution = 0
                        ignoreSolution = True

                if (j < (lengthConstants - 1)):
                    combination += " * "

        # This combination has to be saved. Squared to remove the roots
        if ((units**2).equals(constants[1][1]) == 1):
            if (repeatOperation == True):
                listCombinations.append([combination, solution])
                repeatOperation = False
                ignoreSolution = False
            else:
                repeatOperation = True;
                i -= 1

        i += 1