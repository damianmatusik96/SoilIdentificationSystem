from app.IndentificationSystem.data.DataHandler import DataHandler
from app.IndentificationSystem.data.DataCluster import DataCluster
import pandas as pd


data_handler_1 = DataHandler()
data_handler_1.get_data("sdmt1.csv")
data_handler_2 = DataHandler()
data_handler_2.get_data("sdmt2.csv")
data_handler_3 = DataHandler()
data_handler_3.get_data("sdmt3.csv")

data = pd.concat([data_handler_1.data, data_handler_2.data])
data.reset_index()

data_cluster = DataCluster(data)
data_cluster_3 = DataCluster(data_handler_3.data)
#todo dopracowac pierwszy klaster