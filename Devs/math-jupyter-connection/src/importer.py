#!/usr/bin/env python

import os


class CSVImporter:
    """
    - Import the numerical data inside the given CSV file
    - The CSV file is represented by a string (path to the actual file) and it is given as a class argument when first initializing the class itself
    - First the data is imported in raw-format
    - Additional function for parsing the raw data into proper format that can be furthermore graphically represented is also implemented
    """

    def __init__(self):
        """
        - At init, the class receives the path to the csv file
        - Numerical data will be imported from that path
        """
        # fix the path to the data directory in which all the csv files are stored
        ROOTDIR = str(os.getcwd()) + '/../'
        DATA_DIR_NAME = 'data'
        DATA_DIR_PATH = ROOTDIR + DATA_DIR_NAME + '/'
        # get every csv file name within the datadir
        # append the proper path to the file name
        CSV_FILES = [str(DATA_DIR_PATH) +
                     fl for fl in os.listdir(DATA_DIR_PATH) if ".csv" in fl]

        # CSV_FILES.append('FAILER')

        # if there is only one file, create a testing procedure for that particular file
        # otherwise, stop further function calls and just return the content of the data directory
        if(len(CSV_FILES) == 1):
            self.TEST_RUNTIME = True
        else:
            print(
                'There is more than one csv file within the data directory...Stopping the test execution')
            self.TEST_RUNTIME = False

        if(self.TEST_RUNTIME is True):
            self.csv_file_path = CSV_FILES[0]

    def show(self, object):
        try:
            assert object is not None
        except AssertionError as err:
            return -1
        else:
            print(f'{object}')

    def get_param_number(self):
        # only execute the procedure of the init function has a valid runtime value
        if(self.TEST_RUNTIME is False):
            return -1

        with open(self.csv_file_path, 'r+') as reader:
            first_line = reader.readline()
        commas = [l for l in first_line if l == ","]
        param_set_number = int((len(commas) + 1) / 2)

        return param_set_number

    def get_param_values(self):
        # only execute the procedure of the init function has a valid runtime value
        if(self.TEST_RUNTIME is False):
            return -1

        raw_params = []

        # stop if the `raw_params` array has dimension != 1
        try:
            assert len(raw_params) == 1
        except AssertionError as err:
            return -1
        finally:
            pass

        with open(self.csv_file_path, 'r+') as reader:
            for idx in range(2):
                current_line = next(reader).strip()
                if(idx == 1):
                    raw_params.append(current_line)

        params = [int(p) for p in raw_params[0].split(',')]
        param_pairs = [[params[id], params[id + 1]]
                       for id in range(0, len(params) - 1, 2)]

        return param_pairs

    def get_legends(self):
        """
        - retrieves the legends that will be used within the graphical representations
        - legends are represented in the csv file as text labels, after the numerical values of the parameters 
        """

        # only execute the procedure of the init function has a valid runtime value
        if(self.TEST_RUNTIME is False):
            return -1

        # retrieve the fourth line within the csv file
        with open(self.csv_file_path, 'r+') as reader:
            for idx in range(0, 3, 1):
                current_line = next(reader).strip()
                if(idx == 2):
                    legends = current_line.split(',')[:2]

        # clean the two legends in order to get rid of the extra quotes
        legends[0] = str(legends[0][1])
        legends[1] = str(legends[1][1:-1])

        # print(legends)

        return legends

    def get_raw_data(self):
        """
        - retrieve the numerical data from the csv file
        - data is stored in an array of arrays (where each sub-array represents a line of numbers)
        - data is stored as a so-called **raw format** where no change on the structure of the columns is performed
        """

        # only execute the procedure of the init function has a valid runtime value
        if(self.TEST_RUNTIME is False):
            return -1

        with open(self.csv_file_path, 'r+') as reader:
            raw_lines = reader.readlines()[3:]

        # perform some cleaning of the extracted data
        # no parsing
        cleaned_data = [raw_line.strip().split(',')
                        for raw_line in raw_lines]

        return cleaned_data

    def numerical_data(self):
        """
        - perform PARSING & RESTRUCTURING of the extracted raw data to float
        - restructure the numerical data in such a way that each pair of elements from a sub-array corresponds to a single parameter set: x,f(x)
        """

        # only execute the procedure of the init function has a valid runtime value
        if(self.TEST_RUNTIME is False):
            return -1

        # map the float function to any object that is iterable
        floater = lambda object: list(map(float, object))

        raw_data = self.get_raw_data()
        float_data = [floater(raw_line) for raw_line in raw_data]

        # delete the initial array after float has been performed
        # source: https://www.kite.com/python/answers/how-to-delete-an-array-in-python
        del raw_data

        # determine the number of pairs {x,f(x)} for the entire csv file
        # determine the length of a dataset
        data_set_size = len(float_data)
        number_of_function_pairs = int(len(float_data[0]) / 2)

        rows = data_set_size
        columns = len(float_data[0])

        full_data_set = []

        for col in range(0, columns - 1, 2):
            current_data_set = []
            for row in range(rows):
                current_pair = [float_data[row][col], float_data[row][col + 1]]
                current_data_set.append(current_pair)
            full_data_set.append(current_data_set)

        return full_data_set

    def get_column_pair(self, pair_id):
        """
        - retrieve only the i-th pair of columns {x,f(x)} from the csv file and prepare the data for graphical representation
        """
        # continue only of the pair index is no greater than the total number of pairs
        numerical_data = self.numerical_data()
        print(len(numerical_data))
        try:
            assert pair_id <= len(numerical_data)
        except AssertionError as err:
            return -1
        else:
            return numerical_data[pair_id - 1]

        # pure data retriever
        with open(self.csv_file_path)


def main():
    print(f'Main function of the importer module...')


if __name__ == "__main__":
    main()
