#!/usr/bin/env python

import importer as csv
import os

# constants and relevant parameters/arguments that will be used throughout execution
DATADIRNAME = "data/"
DATADIRPATH = str(os.getcwd())[0:-3] + DATADIRNAME
CSVFILES = [file for file in os.listdir(DATADIRPATH) if ".csv" in file]
CSV_1 = CSVFILES[0]
# conditional for printing the data to console (1) or not (0)
PRINT_TO_SCREEN = 0


# lambda for appending the data directory path to the csf file name
csvfilepath = lambda filename: f'{DATADIRPATH}{filename}'


def printer(main_cls, main_obj):
    for obj in main_obj:
        main_cls.show(obj)


# This is the main (executable) app...
def main(print_condition):
    file = csv.CSVImporter(csvfilepath(CSV_1))
    n_params = file.get_param_number()
    param_values = file.get_param_values()
    legends = file.get_legends()
    raw_data = file.get_raw_data()
    numerical_data = file.numerical_data()

    if(print_condition == 1):
        # print the data to the console
        obj_list = [n_params, param_values, legends, raw_data, numerical_data]
        printer(file, obj_list)


if __name__ == "__main__":
    main(PRINT_TO_SCREEN)
