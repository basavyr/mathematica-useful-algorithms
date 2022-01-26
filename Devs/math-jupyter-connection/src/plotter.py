#!/usr/bin/env python

from matplotlib import pyplot as plt
import os


class Plotter:

    def self_check_data(self, data):
        """
        - check if the data is invalid (i.e., empty array or non-existing object)
        """
        try:
            assert len(data) > 0
        except Exception as err:
            return -1
        else:
            return 1

    def __init__(self, data):
        """
        - get the numerical data from the csv file
        - plot the numerical data and save it as a pdf file within the same location as the csv file
        - data is parsed and restructured
        """
        if(self.self_check_data(data) == 1):
            self.numerical_data = data
            print(f'Initializing numerical data ✅')
        else:
            print(f'Initializing numerical data ❌')

    def generate_plot_files(self):
        """
        - generates all the filenames for the data sets retrieved from the csv file
        - the number of filenames depend on the number of sub-arrays within the initial (parsed) numerical data
        - numerical data is provided by the importer model
        """
        file_name = lambda idx: f'dataplot_{idx}.pdf'
        file_names = [file_name(idx + 1)
                      for idx in range(len(self.numerical_data))]
        return file_names

    def plot_path(self, filenames):
        DATA_DIR = 'data/'
        data_dir_path = lambda file_name: str(
            os.getcwd()) + '/../' + DATA_DIR + str(file_name)

        file_paths = [data_dir_path(x) for x in filenames]

        return file_paths

    def plot_column_data(self, idx, params_idx, legends):
        """ 
        - plot a single pair {x,f(x)} from the tabular data
        - the file name of the plot corresponds to the idx-th element of the array with pre-generated file names
        - idx => [1,2,3...,len(numerical_data)]
        """
        numerical_data = self.numerical_data
        try:
            assert idx <= len(numerical_data)
        except Exception as err:
            return -1
        plot_name = self.generate_plot_files()[idx - 1]
        plot_path = self.plot_path(self.generate_plot_files())[idx - 1]

        x_data = [x[0] for x in numerical_data[idx - 1]]
        y_data = [x[1] for x in numerical_data[idx - 1]]

        # fig, ax = plt.subplots()

        # plt.plot(x_data, y_data, '-r', label=r'$m_{func}$')
        # plt.xlabel(legends[0])
        # plt.ylabel(legends[1])
        # ax.legend(loc='best')
        # ax.set_title('')
        # plt.text(0.80, 0.20, f'(a,b)=({params_idx[0]},{params_idx[1]})', horizontalalignment='center',
        #          verticalalignment='center', transform=ax.transAxes, fontsize=11)
        # plt.savefig(plot_name, bbox_inches='tight', dpi=300)
        # fig.tight_layout()
        # plt.close()

    def plot_numerical_data(self, params, legends):
        """
        - create a graphical representation with all the datasets within the csv table
        """

        numerical_data = self.numerical_data

        for idx in range(len(numerical_data)):
            self.plot_column_data(idx + 1, params[idx], legends)
