#!/usr/bin/env python

class CSVImporter:
    """
    - Import the numerical data inside the given CSV file
    - The CSV file is represented by a string (path to the actual file) and it is given as a class argument when first initializing the class itself
    - First the data is imported in raw-format
    - Additional function for parsing the raw data into proper format that can be furthermore graphically represented is also implemented
    """

    def __init__(self, datadirpath):
        self.datadirpath = datadirpath

    def showDirPath(self):
        print(self.datadirpath)


def main():
    print(f'Main function of the importer module...')


if __name__ == "__main__":
    main()
