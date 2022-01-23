#!/usr/bin/env python

class CSVImporter:
    """
    - Import the numerical data inside the given CSV file
    - The CSV file is represented by a string (path to the actual file) and it is given as a class argument when first initializing the class itself
    - First the data is imported in raw-format
    - Additional function for parsing the raw data into proper format that can be furthermore graphically represented is also implemented
    """

    def __init__(self, csv_file_path):
        """
        - At init, the class receives the path to the csv file
        - Numerical data will be imported from that path
        """
        self.csv_file_path = csv_file_path

    def show_csv_path(self):
        print(self.csv_file_path)

    def get_param_number(self,):
        with open(self.csv_file_path, 'r+') as reader:
            first_line = reader.readline()
        commas = [l for l in first_line if l == ","]
        param_set_number = int((len(commas) + 1) / 2)

        return param_set_number

    def get_param_values(self):
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
        # retrieve the fourth line within the csv file
        with open(self.csv_file_path, 'r+') as reader:
            for idx in range(0, 3, 1):
                current_line = next(reader).strip()
                if(idx == 2):
                    legends = current_line.split(',')[:2]

        # clean the two legends in order to get rid of the extra quotes
        legends[0] = str(legends[0][1])
        legends[1] = str(legends[1][1:-1])
        print(legends)

    def get_raw_data(self):
        """
        - retrieve the numerical data from the csv file
        - data is stored in an array of arrays (where each sub-array represents a line of numbers)
        - data is stored as a so-called **raw format** where no change on the structure of the columns is performed
        """
        with open(self.csv_file_path, 'r+') as reader:
            raw_lines = reader.readlines()[3:]

        # perform some cleaning of the extracted data
        # no parsing
        cleaned_data = [raw_line.strip().split(',')
                        for raw_line in raw_lines]

        return cleaned_data

    def parse_raw_data(self):
        """
        - perform parsing of the extracted raw data to float
        - restructure the numerical data in such a way that each pair of elements from a sub-array corresponds to a single parameter set: x,f(x)
        """
        # map the float function to any object that is iterable
        floater = lambda object: list(map(float, object))

        raw_data = self.get_raw_data()
        float_data = [floater(raw_line) for raw_line in raw_data]

        print(raw_data[0])
        print(float_data[0])


def main():
    print(f'Main function of the importer module...')


if __name__ == "__main__":
    main()
