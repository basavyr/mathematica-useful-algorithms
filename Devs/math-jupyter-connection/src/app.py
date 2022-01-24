#!/usr/bin/env python

import importer as csv
import os

# constants and relevant parameters/arguments that will be used throughout execution
# the directory name in which all the data used for numerical computations are stored
DATADIRNAME = "data"
# the path to the main root directory of the entire project
ROOTPATH = str(os.getcwd()) + '/../'
# path to the data folder
DATADIRPATH = str(os.getcwd())[0:-3] + DATADIRNAME
D_DATADIRPATH = ROOTPATH + DATADIRNAME
CSVFILES = [file for file in os.listdir(DATADIRPATH) if ".csv" in file]
C_CSVFILES = [file for file in os.listdir(D_DATADIRPATH) if ".csv" in file]
CSV_1 = CSVFILES[0]
C_CSV_1 = C_CSVFILES[0]


# conditional for printing the data to console (1) or not (0)
PRINT_TO_SCREEN = 0


# lambda for appending the data directory path to the csf file name
csvfilepath = lambda filename: f'{DATADIRPATH}/{filename}'


# print the objects evaluated from the class methods on the screen
def printer(main_cls, main_obj):
    for obj in main_obj:
        main_cls.show(obj)


# This is the main (executable) app...
def main():
    file = csv.CSVImporter()
    n_params = file.get_param_number()
    param_values = file.get_param_values()
    legends = file.get_legends()
    raw_data = file.get_raw_data()
    numerical_data = file.numerical_data()

    # if(print_condition == 1):
    #     # print the data to the console
    #     obj_list = [n_params, param_values, legends, raw_data, numerical_data]
    #     printer(file, obj_list)


if __name__ == "__main__":
    main()
    # print(csvfilepath(CSV_1))
    # print(csvfilepath(C_CSV_1))
