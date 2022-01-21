#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np
import os
import math

# path to the /data directory
datapath = str(os.getcwd())[:-4] + "/data/"

# get the csv file from the /data directory
csvfiles = [x for x in os.listdir(datapath) if ".csv" in x]
csv1 = csvfiles[0]

# create a function that reads the first line of the csv file and returns the number of parameter sets within the file


def getParams(csv_file):
    """ 
    - the function reads the first line of the csv file
    - the first line is stored in memory, then based on the number of commas, total number of sets is determined
    """
    with open(str(datapath) + str(csv_file), 'r+') as csv_reader:
        firstline = csv_reader.readline()

    Nparams = (len([fl for fl in firstline if fl == ","]) + 1) / 2
    print(Nparams%10)
    return int(Nparams)


Nparams = getParams(csv1)
print(f'There are {Nparams} parameter sets')

# create a function that gets the values for all the parameter sets in the csv file
