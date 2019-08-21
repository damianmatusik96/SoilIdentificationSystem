from app.IndentificationSystem import data_cluster, data_handler_3, data_cluster_3
from WebAppBackend.data.ProfilePredictor import ProfilePredictor
import matplotlib.pyplot as plt


def get_profile():
    data_cluster.choose_best_cluster(2, 8)
    profile_predictor = ProfilePredictor(data_handler_3.raw_data_pr, data_cluster)
    profile_predictor.get_best_profile()
    profile_predictor.sort_data()
    siema = profile_predictor.sorted_data.copy()
    siema['depth'] = data_handler_3.raw_data['depth']
    profile_predictor.sorted_data = siema
    # json_data = profile_predictor.sorted_data.to_json()
    json_data = create_json(profile_predictor.sorted_data)
    return json_data


def create_json(data):
    a = False
    base = '{"groups":{'
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

    base = base + '},"profile":['
    for i in range(0, len(data.values)):
        base = base + '{' + '"x":' + f"{data.at[i, 'labels']}" + ',"y":' + f"{data.at[i, 'depth']}"
        if i == (len(data.values) - 1):
            base = base + "}"
        else:
            base = base + "},"
    base = base + "]}"

    return base

