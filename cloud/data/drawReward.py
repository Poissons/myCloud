from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dqn_data = pd.read_csv(r'./5_22_4/dqn/reward_hist.csv', header=None, names=['index', 'reward_percent'])
    greedy_data = pd.read_csv(r'./5_22_4/greedy/reward_hist.csv', header=None, names=['index', 'reward_percent'])


    plt.title('reward', fontsize=20)
    plt.ylabel(u'成功率', fontsize=10)

    plt.plot(dqn_data['index'], dqn_data['reward_percent'], color='deeppink', linewidth=1.5,  label='dqn')
    plt.plot(greedy_data['index'], greedy_data['reward_percent'], color='darkblue', linewidth=1.5,  label='failure')
    # plt.plot(x, stuck_y, color='goldenrod', linewidth=1, linestyle='-', label='stuck')

    # plt.legend(loc=2)
    plt.savefig('./5_22_4/reward.png')
    plt.show()
