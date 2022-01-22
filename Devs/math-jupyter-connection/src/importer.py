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
    """
    - returns a tuple [l1,l2]
    - contains the first two elements of the third row in the `.csv` file
    """
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


# parse the raw data obtained from the csv file into a proper column-by-column pair `x_i,f(x_i)` with i representing the i-th parameter set
def parsedata(rawdata):
    # stop the function if the rawdata is empty
    try:
        assert len(rawdata) > 0
    except AssertionError as err:
        return -1
    finally:
        pass

    ncols = len(rawdata[0])
    parsed_data = []

    for col_id in range(ncols):
        currentcol = []
        for row_id in range(len(rawdata)):
            currentcol.append(rawdata[row_id][col_id])
        parsed_data.append(currentcol)

    return parsed_data


# plot a single pair of columns (representing the `x,f(x)` numerical data corresponding the a parameter set)
def plotdata(parsed_data, params, legends, datadirpath, idx):
    """
    - The method creates a graphical representation for the two columns `{[x],[f(x)]}`.
    - The `idx` argument fixes the i-th column pair of the numerical data and the parameter set `p_i` that corresponds to that particular
    - the legends are represented by a tuple
    - the plot is saved as pdf within the `datapath` directory
    """
    chosen_id = idx
    column = parsed_data[chosen_id]
    paramset = params[chosen_id]

    # generate a plotfile in pdf format
    plotfile = lambda idx: str(datadirpath) + f'dataplot_{idx}.pdf'

    x_data = [x[0] for x in column]
    y_data = [x[1] for x in column]

    fig, ax = plt.subplots()
    plt.text(0.25, 0.75, f'(a,b) = ({paramset[0]},{paramset[1]})', horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes, fontsize=11)
    plt.plot(x_data, y_data, '-k', label=r'$m_{func}$')
    plt.legend(loc='best')
    plt.xlabel(f'{legends[0]}')
    plt.ylabel(f'{legends[1]}')
    plt.savefig(plotfile(chosen_id), bbox_inches='tight', dpi=300)
    plt.close()


# the main function which will be called @ script runtime
def main():

    # path to the /data directory
    datadirpath = str(os.getcwd())[:-4] + "/data/"

    # get the csv file from the /data directory
    csvfiles = [(str(datadirpath) + str(x))
                for x in os.listdir(datadirpath) if ".csv" in x]

    csv1 = csvfiles[0]

    nparams = getNparams(csv1)
    params = getparams(csv1)
    legends = getlegends(csv1)
    rawT = getrawdata(csv1)
    parsedT = parsedata(rawT)
    plotdata(parsedT, params, legends, datadirpath, 0)
    plotdata(parsedT, params, legends, datadirpath, 1)


if __name__ == "__main__":
    main()
