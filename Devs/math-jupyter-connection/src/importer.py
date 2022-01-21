#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np
import os
import math


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


# create a function that gets the values for all the parameter sets in the csv file
def getparams(csv_file):
    """
    - the function retrieves the numerical values for each pair of parameters given within the csv file
    """
    rawparams = []

    with open(csv_file, 'r+') as reader:
        # get the first two lines of the csv file and store it in memory
        # source: https://stackoverflow.com/questions/1767513/how-to-read-first-n-lines-of-a-file
        for fx in range(2):
            line = next(reader).strip()
            if(fx == 1):
                rawparams.append(line)

    # with the line of parameters stored, extract every integer from the set
    params = rawparams[0]
    params = list(map(int, params.split(',')))

    # with every integer obtained, create pairs of parameters
    # create pairs from the entire parameter sets
    # extracting the numerical values from the entire line of parameters of the csv file
    parampairs = []
    for x in range(0, len(params), 2):
        parampairs.append([int(params[x]), int(params[x + 1])])
    return parampairs


# get the legends for the data set imported from the csv file
def getlegends(csvfile):
    with open(csvfile, 'r+') as reader:
        # store the third line only

        rawlegend = []

        for fx in range(3):
            line = next(reader).strip()
            if(fx == 2):
                rawlegend.append(line)

        legends = rawlegend[0].split(',')
        legend = [legends[0][1:-1], legends[1][1:-1]]
        return legend


# get the numerical data from the csv file
def getrawdata(csvfile):
    """ 
    - the numerical data is retrieved in raw-mode
    - no parsing & data transformation is performed
    """
    rawdata = []

    with open(csvfile, 'r+') as reader:
        content = reader.readlines()[3:]
        for c in content:
            c.strip()
            c = list(map(float, c.split(',')))
            rawdata.append(c)

    rawlines = []
    for rawline_id in range(0, len(rawdata), 1):
        rawline = []
        for line_id in range(0, len(rawdata[0]), 2):
            # a line contains pairs of the form `x_i,f(x_i)` for all the parameter sets `p_i`
            rawline.append([rawdata[rawline_id][line_id],
                            rawdata[rawline_id][line_id + 1]])
        rawlines.append(rawline)

    return rawlines


# parse the raw data obtained from the csv file into a proper column-by-column pair `x_i,f(x_i)` with i representing the i-th parameeter set
def parsedata(rawdata):
    ncols = len(rawdata[0])
    parsed_data = []
    col_id = 0
    for col_id in range(ncols):
        currentcol = []
        for row_id in range(len(rawdata)):
            currentcol.append(rawdata[row_id][col_id])
        parsed_data.append(currentcol)
    print(parsed_data)


def main():
    # path to the /data directory
    datapath = str(os.getcwd())[:-4] + "/data/"

    # get the csv file from the /data directory
    csvfiles = [(str(datapath) + str(x))
                for x in os.listdir(datapath) if ".csv" in x]
    csv1 = csvfiles[0]

    nparams = getNparams(csv1)
    params = getparams(csv1)
    # print(f'There are {nparams} parameters in the csv file')
    # for pair in params:
    #     print(pair)
    # getlegends(csv1)
    rawT = getrawdata(csv1)
    parsedata(rawT)


if __name__ == "__main__":
    main()
