import multiprocessing
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
    pass