#!/usr/bin/env python

import importer as csv
import plotter as plt


# This is the main (executable) app...
def main():
    # import phase
    csv_file = csv.CSVImporter()
    numerical_data = csv_file.numerical_data()
    params = csv_file.get_param_values()
    print(params)
    legends = csv_file.get_legends()

    # plot phase
    plot = plt.Plotter(numerical_data)
    plot.plot_numerical_data(params, legends)
    # trimmed_data = file.trim_numerical_data(5)
    # plot = plt.Plotter(trimmed_data)


if __name__ == "__main__":
    main()
