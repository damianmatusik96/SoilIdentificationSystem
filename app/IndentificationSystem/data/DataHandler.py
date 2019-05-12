import pandas as pd

class DataHandler:
    def __init__(self):
        self.data = None

    def get_data(self, file):
        try:
            data = pd.read_csv("IndentificationSystem\\data\\files\\" + file, sep=";", header=None)
        except:
            print("Cannot open file")
        data.columns = ["a", "b", "c"]
        data_pr = data[["b", "c"]]

        self.data = data_pr

