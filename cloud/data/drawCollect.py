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
    data = pd.read_csv(r'./5/greedy/collect5compute.csv', header=None,
                       names=['success', 'failure', 'stuck', 'success_percent',
                              'failure_percent', 'stuck_percent'])
    x = np.arange(1, data.shape[0]).tolist()
    success_y = data['success_percent'][1:].tolist()
    failure_y = data['failure_percent'][1:].tolist()
    stuck_y = data['stuck_percent'][1:].tolist()

    plt.title(u'任务执行情况统计表', fontsize=20)
    plt.ylabel(u'比例', fontsize=10)

    plt.plot(x, success_y, color='deeppink', linewidth=1.5, linestyle=':', label='success')
    plt.plot(x, failure_y, color='darkblue', linewidth=1.5, linestyle='--', label='failure')
    plt.plot(x, stuck_y, color='goldenrod', linewidth=1, linestyle='-', label='stuck')

    plt.legend(loc=2)
    plt.savefig('./5/greedy/collect5.png')
    plt.show()
