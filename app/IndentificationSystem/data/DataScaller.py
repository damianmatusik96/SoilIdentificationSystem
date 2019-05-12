import pandas as pd
import numpy as np
from scipy import stats
from mlxtend.preprocessing import minmax_scaling
import seaborn as sns
import matplotlib.pyplot as plt

from app.IndentificationSystem import data_handler


class DataScaller:

    def __init__(self, data):
        self.original_data = np.array(data, dtype=np.float)
        self.scaled_data = minmax_scaling(data, columns=[0])
        self.normalized_data = stats.boxcox(data)

    # fig, ax = plt.subplots(1, 2)
    # sns.distplot(original_data, ax=ax[0])
    # ax[0].set_title("Original Data")
    # sns.distplot(scaled_data, ax=ax[1])
    # ax[1].set_title("Scaled Data")

    def show_scaled_data(self):
        fig, ax = plt.subplots(1, 2)
        sns.distplot(self.original_data, ax=ax[0])
        ax[0].set_title("Original Data")
        sns.distplot(self.scaled_data, ax=ax[1])
        ax[1].set_title("Scaled data")
        plt.show()

    def show_normalized_data(self):
        fig, ax = plt.subplots(1, 2)
        sns.distplot(self.original_data, ax=ax[0])
        ax[0].set_title("Original Data")
        sns.distplot(self.normalized_data, ax=ax[1])
        ax[1].set_title("Normalized data")
        plt.show()


