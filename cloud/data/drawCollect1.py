from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib


# import seaborn as sns


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
    data = pd.read_csv(r'./10_21_6/dqn/collect_compute2.csv')
    plt.title('tasks execution situation')
    plt.stackplot(
        np.arange(len(data['success_percent'])),
        data['success_percent'], data['stuck_percent'], data['failure_percent'],
        labels=('success', 'stuck', 'failure'),
        colors=('orange', 'lightgreen', 'lightblue'),
    )
    plt.xlim(0, len(data['success_percent']) - 1)
    plt.ylim(0, 1)
    plt.legend()
    plt.show()
