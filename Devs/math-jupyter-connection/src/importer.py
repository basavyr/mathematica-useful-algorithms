#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np
import os
import math


# path to the /data directory
datapath = str(os.getcwd())[:-4] + "/data/"


# get the csv file from the /data directory
csvfiles = [(str(datapath) + str(x))
            for x in os.listdir(datapath) if ".csv" in x]
csv1 = csvfiles[0]


def isodd(number):
    """check if the number is odd"""
    try:
        assert number % 2 != 0
    except AssertionError as err:
        return 0
    return 1


# create a function that reads the first line of the csv file and returns the number of parameter sets within the file
def getNparams(csv_file):
    """
    - the function reads the first line of the csv file
    - the first line is stored in memory, then based on the number of commas, total number of sets is determined
    """

    with open(csv_file, 'r+') as csv_reader:
        firstline = csv_reader.readline()

    # perform a check for correct number of commas
    Ncommas = len([fl for fl in firstline if fl == ","])
    if(isodd(Ncommas) == 0):
        return -1
    else:
        Nparams = int((Ncommas + 1) / 2)

    return Nparams


print(f'There are {getNparams(csv1)} parameters in the csv file')

# create a function that gets the values for all the parameter sets in the csv file


def getparams(csv_file):
    """
    - the function retrieves the numerical values for each pair of parameters given within the csv file
    """
    params = []

    with open(csv_file, 'r+') as reader:
        # get the first two lines of the csv file and store it in memory
        # source: https://stackoverflow.com/questions/1767513/how-to-read-first-n-lines-of-a-file
        params = []
        for fx in range(2):
            line = next(reader).strip()
            if(fx == 1):
                params.append(line)
    return params[0]


print(getparams(csv1))
# getparams(csv1)
