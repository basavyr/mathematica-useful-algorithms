#!/usr/bin/env python

import importer as csv

# print the data to the console
PRINT_TO_SCREEN = 0


# print the objects evaluated from the class methods on the screen
def printer(main_cls, main_obj):
    for obj in main_obj:
        main_cls.show(obj)


# This is the main (executable) app...
def main():
    file = csv.CSVImporter()
    # n_params = file.get_param_number()
    # param_values = file.get_param_values()
    # legends = file.get_legends()
    # raw_data = file.get_raw_data()
    # numerical_data = file.numerical_data()
    # column_pair = file.get_column_pair(1)
    trimmed_data = file.trim_numerical_data(10)

    if(PRINT_TO_SCREEN == 1):
        # obj_list = [n_params, param_values, legends, raw_data, numerical_data]
        obj_list = [trimmed_data]
        printer(file, obj_list)


if __name__ == "__main__":
    main()
