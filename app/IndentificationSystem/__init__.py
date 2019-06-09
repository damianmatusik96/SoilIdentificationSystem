from app.IndentificationSystem.data.DataHandler import DataHandler
from app.IndentificationSystem.data.DataCluster import DataCluster
import pandas as pd


data_handler_1 = DataHandler()
data_handler_1.get_data("sdmt1.csv")

data_handler_2 = DataHandler()
data_handler_2.get_data("sdmt2.csv")

data_handler_3 = DataHandler()
data_handler_3.get_data("sdmt3.csv")

data3 = data_handler_3.data
data3_pr = data3[['param_1', 'param_2']]
data_handler_3.data = data3_pr

data = pd.concat([data_handler_1.data, data_handler_2.data])

reset_index_data = data.reset_index()
prepared_data = reset_index_data.sort_values('depth')
final_data = prepared_data.reset_index()

datapr = final_data[['param_1', 'param_2']]

data_cluster = DataCluster(datapr)

data_cluster_3 = DataCluster(data_handler_3.data)
#todo dopracowac pierwszy klaster