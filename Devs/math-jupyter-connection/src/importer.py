#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np
import os

# path to the /data directory
datapath=str(os.getcwd())[:-4]+"/data/"

#get the csv file from the /data directory
csvfiles=[x for x in os.listdir(datapath) if ".csv" in x]
csv1=csvfiles[0]

# create the importer function
def importCSV(csv_file):
    with open(str(datapath)+str(csv_file),'r+') as csv_reader:
        firstline=csv_reader.readline()

    return firstline

firstline=importCSV(csv1)
Ncommas=len([x for x in importCSV(csv1) if x==","])
Nparams=(Ncommas+1)/2
print(f'There are {Nparams} parameter sets')