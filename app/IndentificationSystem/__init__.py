from app.IndentificationSystem.data.DataHandler import DataHandler
from app.IndentificationSystem.data.DataCluster import DataCluster



data_handler_1 = DataHandler()
data_handler_1.get_data("sdmt1.csv")
data_handler_2 = DataHandler()
data_handler_2.get_data("sdmt2.csv")
data_handler_3 = DataHandler()
data_handler_3.get_data("sdmt3.csv")

data_cluster_1 = DataCluster(data_handler_1.data)
data_cluster_2 = DataCluster(data_handler_2.data)
data_cluster_3 = DataCluster(data_handler_3.data)
