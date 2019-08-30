from app.IndentificationSystem import data_cluster, data_handler_3, data_cluster_3
from WebAppBackend.data.ProfilePredictor import ProfilePredictor
import matplotlib.pyplot as plt


def get_profile():
    data_cluster.choose_best_cluster(2, 8)
    data_cluster_3.choose_best_cluster(2, 8)
    data_cluster_3.sort_data()
    profile_predictor = ProfilePredictor(data_handler_3.raw_data_pr, data_cluster)
    profile_predictor.get_best_profile()
    profile_predictor.sort_data()
    siema = profile_predictor.sorted_data.copy()
    siema['depth'] = data_handler_3.raw_data['depth']
    profile_predictor.sorted_data = siema
    elo = data_cluster_3.sorted_data.copy()
    elo['depth'] = data_handler_3.raw_data['depth']
    data_cluster_3.sorted_data = elo
    json_data = create_json(profile_predictor.sorted_data, data_cluster_3.sorted_data)
    return json_data


def create_json(data, avg_data):
    a = False
    base = '{"groups1":{'
    base = base + '"group1":['
    for i in range(0, len(data.values)):
        if data.at[i, 'labels'] == 0:
            base = base + '{' + '"x":' + f"{data.at[i, 'param_1']}" + ',"y":' + f"{data.at[i, 'param_2']}"
            base = base + "},"
        else:
            base = base[:-1] + "],"
            a = False
            break

    base = base + '"group2":['
    for i in range(0, len(data.values)):
        if data.at[i, 'labels'] == 1:
            base = base + '{' + '"x":' + f"{data.at[i, 'param_1']}" + ',"y":' + f"{data.at[i, 'param_2']}"
            base = base + "},"
            a = True
        elif a:
            base = base[:-1] + "],"
            a = False
            break
    base = base + '"group3":['
    for i in range(0, len(data.values)):
        if data.at[i, 'labels'] == 2:
            base = base + '{' + '"x":' + f"{data.at[i, 'param_1']}" + ',"y":' + f"{data.at[i, 'param_2']}"
            base = base + "},"
        if i == (len(data.values) - 1):
            base = base[:-1] + "]"
            break

    base = base + '},"profile1":['
    for i in range(0, len(data.values)):
        base = base + '{' + '"x":' + f"{data.at[i, 'labels']}" + ',"y":' + f"{data.at[i, 'depth']}"
        if i == (len(data.values) - 1):
            base = base + "}"
        else:
            base = base + "},"
    base = base + "],"


    a = False
    base = base + '"groups2":{'
    base = base + '"group1":['
    for i in range(0, len(avg_data.values)):
        if avg_data.at[i, 'labels'] == 0:
            base = base + '{' + '"x":' + f"{avg_data.at[i, 'param_1']}" + ',"y":' + f"{avg_data.at[i, 'param_2']}"
            base = base + "},"
        else:
            base = base[:-1] + "],"
            a = False
            break

    base = base + '"group2":['
    for i in range(0, len(avg_data.values)):
        if avg_data.at[i, 'labels'] == 1:
            base = base + '{' + '"x":' + f"{avg_data.at[i, 'param_1']}" + ',"y":' + f"{avg_data.at[i, 'param_2']}"
            base = base + "},"
            a = True
        elif a:
            base = base[:-1] + "],"
            a = False
            break
    base = base + '"group3":['
    for i in range(0, len(avg_data.values)):
        if avg_data.at[i, 'labels'] == 2:
            base = base + '{' + '"x":' + f"{avg_data.at[i, 'param_1']}" + ',"y":' + f"{avg_data.at[i, 'param_2']}"
            base = base + "},"
        if i == (len(data.values) - 1):
            base = base[:-1] + "],"
            break

    base = base + '"group4":['
    for i in range(0, len(avg_data.values)):
        if avg_data.at[i, 'labels'] == 3:
            base = base + '{' + '"x":' + f"{avg_data.at[i, 'param_1']}" + ',"y":' + f"{avg_data.at[i, 'param_2']}"
            base = base + "},"
        if i == (len(data.values) - 1):
            base = base[:-1] + "]"
            break

    base = base + '},"profile2":['
    for i in range(0, len(avg_data.values)):
        base = base + '{' + '"x":' + f"{avg_data.at[i, 'labels']}" + ',"y":' + f"{avg_data.at[i, 'depth']}"
        if i == (len(avg_data.values) - 1):
            base = base + "}"
        else:
            base = base + "},"
    base = base + "]}"

    return base

