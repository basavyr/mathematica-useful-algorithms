#!/usr/bin/env python

import importer as csv
import plotter as plt


# This is the main (executable) app...
def main():
    file = csv.CSVImporter()
    numerical_data = file.numerical_data()
    # trimmed_data = file.trim_numerical_data(5)
    # plot = plt.Plotter(trimmed_data)
    # plot.plot_numerical_data()


if __name__ == "__main__":
    main()
