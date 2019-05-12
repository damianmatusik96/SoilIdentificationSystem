from sklearn_extensions.fuzzy_kmeans import FuzzyKMeans
import numpy as np
from app.IndentificationSystem import data_handler
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score as ss
from app.IndentificationSystem.data.DataHandler import DataHandler

all_data = list()

for x in range(0, len(data_handler.param1)):
    all_data.append(list([data_handler.param1[x], data_handler.param2[x]]))

data = np.array(all_data)
datapd = pd.DataFrame(data)
scores = []


# for k in range(2, 10):
k=4
fuzzy_kmeans = FuzzyKMeans(k=k, m=4, max_iter=300)
fuzzy_kmeans.fit(datapd)
datapd['labels'] = pd.Series(fuzzy_kmeans.labels_)
score = ss(datapd[[0, 1]], labels=datapd['labels'])
scores.append(score)
#
# datapd.plot.scatter(x=0, y=1, c='labels', colormap='viridis')
# plt.xlabel("Param 1")
# plt.ylabel("Param2")
# plt.title(f'K = {k}, Silhouette score = {score}')

for center in fuzzy_kmeans.cluster_centers_:
    plt.plot(center[0], center[1], 'ro')

# for datapd['labels']
group_data = datapd.groupby(pd.Series(fuzzy_kmeans.labels_), group_keys=datapd['labels'].unique())
# print(datapd)
# print(group_data[1].get_group(1))



# n = [i for i in range(2, 10)]
# plt.figure()
# plt.plot(n, scores)
# plt.xlabel("K")
# plt.ylabel("Silhouette score")
# plt.show()




second_data = DataHandler()
second_data.open_file("files\\sdmt3.txt")
second = list()

for x in range(0, len(data_handler.param1)):
    second.append(list([data_handler.param1[x], data_handler.param2[x]]))

sec_data = np.array(second)
sec_datapd = pd.DataFrame(sec_data)
scores = []
# print(second_data.param1)
max_values = []
min_values = []
for group_label in datapd['labels'].unique():
    max_param1 = np.max(group_data[0].get_group(group_label))
    max_param2 = np.max(group_data[1].get_group(group_label))
    min_param1 = np.min(group_data[0].get_group(group_label))
    min_param2 = np.min(group_data[1].get_group(group_label))
    tuple_max = (max_param1, max_param2)
    tuple_min = (min_param1, min_param2)
    max_values.append(tuple_max)
    min_values.append(tuple_min)
# print(max_values)
# print(min_values)
# print(sec_datapd)

sec_datapd['labels'] = pd.Series(fuzzy_kmeans.labels_)

sec_datapd.set_value(2, 'labels', 50)


print(sec_datapd)
for i in range(0,40):
    for j in range(len(max_values)):
        x,y,z = sec_datapd.values[i]
        max1, max2 = max_values[j]
        min1, min2 = min_values[j]
        # print(x,y)
        if x > min1 and x < max1 and y > min2 and y < max2:
            sec_datapd.set_value(i, 'labels', j)

sec_score = ss(sec_datapd[[0, 1]], labels=sec_datapd['labels'])

print(sec_datapd)
sec_datapd.plot.scatter(x=0, y=1, c='labels', colormap='viridis')
plt.xlabel("Param 1")
plt.ylabel("Param2")
plt.title(f'K = {k}, Silhouette score = {sec_score}')
plt.show()