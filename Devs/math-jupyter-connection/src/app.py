#!/usr/bin/env python

import importer as csv
import plotter as plt


# This is the main (executable) app...
def main():
    file = csv.CSVImporter()
    numerical_data = file.numerical_data()
    plot = plt.Plotter(numerical_data)
    plot.plot_column_data(1)
    plot.plot_column_data(2)


if __name__ == "__main__":
    main()
