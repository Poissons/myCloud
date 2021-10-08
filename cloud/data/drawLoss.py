from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


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
    data = prepare_data(r'./poisson/10_21_6/dqn/loss_hist.csv')
    plt.title('Loss')

    sns.lineplot(data=data['loss'], label="loss")

    plt.xlim(0, len(data['loss']) - 1)

    plt.savefig('./poisson/10_21_6/dqn/loss.png')
    plt.show()
