from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib


def prepare_data(path):
    data = pd.read_csv(path, header=None, names=['epoch', 'reward_percent'])
    num = 0
    for index, row in data.iterrows():
        num += row['reward_percent']
        if index % 10 == 9:
            data.loc[index, 'reward_percent'] = num / 10
            num = 0
    data = data[data.index % 10 == 9]
    data.reset_index(drop=True, inplace=True)
    print(data)
    return data


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dqn_path = r'./10_21_6/dqn/reward_hist.csv'
    dqn_data = prepare_data(dqn_path)
    greedy_path = r'./10_21_6/greedy/reward_hist.csv'
    greedy_data = prepare_data(greedy_path)

    plt.title('reward', fontsize=20)
    plt.ylabel(u'成功率', fontsize=10)

    plt.plot(dqn_data['epoch'], dqn_data['reward_percent'], color='darkblue', linewidth=1.5, label='dqn')
    plt.plot(greedy_data['epoch'], greedy_data['reward_percent'], color='deeppink', linewidth=1.5, label='greedy')

    plt.legend(loc=2)
    plt.savefig('./10_21_6/reward.png')
    plt.show()
