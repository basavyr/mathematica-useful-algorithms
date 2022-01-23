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
    param_values = file.get_param_values()
    legends = file.get_legends()
    raw_data = file.get_raw_data()
    numerical_data = file.numerical_data()
    print(numerical_data)

if __name__ == "__main__":
    main()
