#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np
import os

# path to the /data directory
datapath=str(os.getcwd())[:-4]+"/data/"

#get the csv file from the /data directory
csvfiles=[x for x in os.listdir(datapath) if ".csv" in x]


# create the importer function
def importCSV(csv_file):
    with open(str(datapath)+str(csv_file),'r+') as csv_reader:
        firstline=csv_reader.readline()

    return firstline

nocommas=importCSV(csvfiles[0])
nocommas[0:3]