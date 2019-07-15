import pandas as pd


class DataHandler:
    def __init__(self):
        self.raw_data = None
        self.raw_data_pr = None
        self.sorted_data = None
        self.sorted_data_pr = None

    def get_data(self, *files):
        list = []
        for file in files:
            try:
                filepath = "/home/damian/PycharmProjects/SoilIdentificationSystem-1.0/" \
                           "app/IndentificationSystem/WebAppBackend/data/files/" + file
                data = pd.read_csv(filepath, sep=";", header=None)
                list.append(data)
            except IOError as e:
                print(f'Cannot open file. {e}')
        concated_data = pd.concat(list)
        concated_data.columns = ["depth", "param_1", "param_2"]

        self.raw_data_pr = concated_data[["param_1", "param_2"]]
        self.raw_data = concated_data

        if len(list) > 1:
            self.sort_data()

    def sort_data(self):
        data = self.raw_data.copy()
        reset_index_data = data.reset_index()
        prepared_data = reset_index_data.sort_values('depth')
        final_data = prepared_data.reset_index()

        self.sorted_data = final_data[['depth', 'param_1', 'param_2']]
        self.sorted_data_pr = final_data[['param_1', 'param_2']]
