#!/usr/bin/env python

class CSVImporter:
    """
    - Import the numerical data inside the given CSV file
    - The CSV file is represented by a string (path to the actual file) and it is given as a class argument when first initializing the class itself
    - First the data is imported in raw-format
    - Additional function for parsing the raw data into proper format that can be furthermore graphically represented is also implemented
    """

    def __init__(self, csv_file_path):
        """at init, the class receives the path to the csv file
        numerical data will be imported from that path
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

        with open(self.csv_file_path, 'r+') as reader:
            for idx in range(2):
                current_line = next(reader).strip()
                if(idx == 1):
                    raw_params.append(current_line)

        # stop if the `raw_params` array has dimension != 1
        try:
            assert len(raw_params) == 1
        except AssertionError as err:
            return -1
        finally:
            pass

        params = [int(p) for p in raw_params[0].split(',')]
        param_pairs = [[params[id], params[id + 1]]
                       for id in range(0, len(params) - 1, 2)]
        

        return param_pairs


def main():
    print(f'Main function of the importer module...')


if __name__ == "__main__":
    main()
