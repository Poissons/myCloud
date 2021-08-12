import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv(r'./5_21_6/greedy/collect.csv', header=None, names=['success', 'failure', 'stuck'])
    # data = pd.read_csv(r'./10_21_6/dqn/collect.csv', header=None, names=['success', 'failure', 'stuck'])

    success_percent = []
    failure_percent = []
    stuck_percent = []

    for row in data.iterrows():
        success = row[1]['success']
        failure = row[1]['failure']
        stuck = row[1]['stuck']
        if success == 0 and failure == 0 and stuck == 0:
            success_percent.append(0)
            failure_percent.append(0)
            stuck_percent.append(0)
        else:
            success_percent.append(round(success / (success + failure + stuck), 4))
            failure_percent.append(round(failure / (success + failure + stuck), 4))
            stuck_percent.append(round(stuck / (success + failure + stuck), 4))
    data['success_percent'] = success_percent
    data['failure_percent'] = failure_percent
    data['stuck_percent'] = stuck_percent
    data.to_csv('./5_21_6/greedy/collect_compute.csv', index=False)
    # data.to_csv('./10_21_6/dqn/collect_compute.csv', index=False)
