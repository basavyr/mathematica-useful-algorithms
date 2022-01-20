#!/usr/bin/env python
from matplotlib import pyplot as plt
import numpy as np
import os

# path to the /data directory
datapath=str(os.getcwd())[:-4]+"/data/"

# create the importer function
def importCSV(csv_file):
    with open(csv_file,'r+') as csv_reader:
        firstline=csv_reader.readline()
    return firstline
