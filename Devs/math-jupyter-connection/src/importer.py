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

# check if the number is odd


def isodd(number):
    try:
        assert number % 2 != 0
    except AssertionError as err:
        return 0
    return 1


# create a function that reads the first line of the csv file and returns the number of parameter sets within the file
def getParams(csv_file):
    """
    - the function reads the first line of the csv file
    - the first line is stored in memory, then based on the number of commas, total number of sets is determined
    """

    with open(str(datapath) + str(csv_file), 'r+') as csv_reader:
        firstline = csv_reader.readline()

    # perform a check for correct number of commas
    Ncommas = len([fl for fl in firstline if fl == ","])
    if(isodd(Ncommas) == 0):
        return -1
    else:
        Nparams = int((Ncommas + 1) / 2)

    return Nparams


# create a function that gets the values for all the parameter sets in the csv file
