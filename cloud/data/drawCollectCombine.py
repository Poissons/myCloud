from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib


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
    greedy_data = pd.read_csv(r'./10_21_6/greedy/collect_compute.csv', header=None,
                              names=['success', 'failure', 'stuck', 'success_percent',
                                     'failure_percent', 'stuck_percent'])
    dqn_data = pd.read_csv(r'./10_21_6/dqn/collect_compute.csv', header=None,
                           names=['success', 'failure', 'stuck', 'success_percent',
                                  'failure_percent', 'stuck_percent'])
    x = np.arange(1, dqn_data.shape[0]).tolist()
    greedy_y = greedy_data['success_percent'][1:].tolist()
    dqn_y = dqn_data['success_percent'][1:].tolist()

    plt.title(u'任务执行情况统计表', fontsize=20)
    plt.ylabel(u'比例', fontsize=10)

    plt.plot(x, greedy_y, color='deeppink', linewidth=1.5, linestyle=':', label='greedy')
    plt.plot(x, dqn_y, color='darkblue', linewidth=1.5, linestyle='--', label='dqn')

    plt.legend(loc=2)
    plt.savefig('./10_21_6/collect.png')
    plt.show()
