from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns


def is_update(y_total):
    total_length = len(y_total)
    chosen_y = []
    chosen_x = []
    for i in range(1, total_length + 1):
        if y_total[i - 1] == '0.0':
            chosen_y.append(y_total[i])
            chosen_x.append(i)

    return chosen_x, chosen_y


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    greedy_data = pd.read_csv(r'./10_21_6/greedy/collect_compute.csv', usecols=[3])
    dqn_data = pd.read_csv(r'./10_21_6/dqn/collect_compute.csv', usecols=[3])

    plt.title('tasks execution situation')
    plt.ylabel('percent')

    sns.lineplot(data=dqn_data['success_percent'], label="dqn")
    sns.lineplot(data=greedy_data['success_percent'], label="greedy")

    plt.savefig('./10_21_6/collect.png')
    plt.show()
