from app.IndentificationSystem.data.DataHandler import DataHandler
from app.IndentificationSystem.data.DataCluster import DataCluster



data_handler = DataHandler()
data_handler.get_data("sdmt3.csv")
data_cluster = DataCluster(data_handler.data)