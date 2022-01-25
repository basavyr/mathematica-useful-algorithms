#!/usr/bin/env python

from matplotlib import pyplot as plt


class Plotter:

    def check_data(self, data):
        """
        - check if the data is invalid (i.e., empty array or non-existing object)
        """
        try:
            assert(len(data) > 0 or data is not None)
        except Exception as err:
            return -1
        else:
            return 1

    def __init__(self, data):
        """
        - get the numerical data from the csv file
        - plot the numerical data and save it as a pdf file within the same location as the csv file
        - data is parsed and restructured
        """
        if(self.check_data(data) == 1):
            self.numerical_data = data
            print(f'All good.')
