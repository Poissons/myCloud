from matplotlib import pyplot as plt
import pandas as pd


def prepare_data(path):
    data = pd.read_csv(path, header=None, names=['epoch', 'loss'])
    num = 0
    for index, row in data.iterrows():
        num += row['loss']
        if index % 10 == 9:
            data.loc[index, 'loss'] = num / 10
            num = 0
    data = data[data.index % 10 == 9]
    data.reset_index(drop=True, inplace=True)
    print(data)
    return data


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    data = prepare_data(r'./10_21_6/dqn/loss_hist.csv')
    plt.title('Loss', fontsize=20)
    plt.ylabel(u'loss', fontsize=10)

    plt.plot(data['epoch'], data['loss'], color='deeppink', linewidth=1.5)

    plt.savefig('./10_21_6/dqn/loss.png')
    plt.show()
