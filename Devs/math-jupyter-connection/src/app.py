#!/usr/bin/env python

import importer as csv


# This is the main (executable) app...
def main():
    file = csv.CSVImporter()
    trimmed_data = file.trim_numerical_data(30)


if __name__ == "__main__":
    main()
