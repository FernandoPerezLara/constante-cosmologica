#!/usr/bin/env python

from itertools import combinations
import os
from datetime import datetime
import multiprocessing

from scripts import *

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
    print("Numero de combinaciones:", len(combinations))

    saveCombinations(combinations)

def saveCombinations(combinations):
    pass

main()