#!/usr/bin/env python

import importer as csv
import os

# constants and relevant parameters/arguments that will be used throughout execution
DATADIRNAME = "data/"
DATADIRPATH = str(os.getcwd())[0:-3] + DATADIRNAME
CSVFILES = [file for file in os.listdir(DATADIRPATH) if ".csv" in file]
CSV_1 = CSVFILES[0]

# lambda for appending the data directory path to the csf file name
csvfilepath = lambda filename: f'{DATADIRPATH}{filename}'


# This is the main (executable) app..
def main():
    file = csv.CSVImporter(csvfilepath(CSV_1))
    n_params = file.get_param_number()
    # print(n_params)
    param_values = file.get_param_values()
    print(param_values)


if __name__ == "__main__":
    main()
