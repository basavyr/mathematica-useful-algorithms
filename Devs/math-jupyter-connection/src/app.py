#!/usr/bin/env python

import importer as csv
import plotter as plt


# This is the main (executable) app...
def main():
    file = csv.CSVImporter()
    plot = plt.Plotter([])


if __name__ == "__main__":
    main()
