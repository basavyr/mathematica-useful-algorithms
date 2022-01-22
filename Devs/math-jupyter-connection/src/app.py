#!/usr/bin/env python

import importer as csv
import os

# constants and relevant parameters/arguments that will be used throughout execution
DATADIRNAME = "data/"
DATADIRPATH = str(os.getcwd())[0:-3] + DATADIRNAME


# This is the main (executable) app..
def main():
    file = csv.CSVImporter(DATADIRPATH)
    file.showDirPath()


if __name__ == "__main__":
    main()
