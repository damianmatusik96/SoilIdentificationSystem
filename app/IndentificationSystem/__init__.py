from app.IndentificationSystem.data.DataHandler import DataHandler
from app.IndentificationSystem.data.DataCluster import DataCluster
import pandas as pd


data_handler_3 = DataHandler()
data_handler_3.get_data("sdmt3.csv")

datah = DataHandler()
datah.get_data("sdmt1.csv", "sdmt2.csv")

data_cluster = DataCluster(datah.sorted_data_pr)

data_cluster_3 = DataCluster(data_handler_3.raw_data_pr)
#todo dopracowac pierwszy klaster