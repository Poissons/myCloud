import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv(r'./no_offload/10_21_6/dqn/collect.csv', header=None, names=['success', 'failure', 'stuck'])
    # data = pd.read_csv(r'./poisson/10_21_6/greedy/collect.csv', header=None, names=['success', 'failure', 'stuck'])

    success_percent = []
    failure_percent = []

    for row in data.iterrows():
        success = row[1]['success']
        failure = row[1]['failure']
        if success == 0 and failure == 0:
            success_percent.append(0)
            failure_percent.append(0)
        else:
            success_percent.append(round(success / (success + failure), 4))
            failure_percent.append(round(failure / (success + failure), 4))
    data['success_percent'] = success_percent
    data['failure_percent'] = failure_percent
    # data.to_csv('./10_21_6/greedy/collect_compute.csv', index=False)
    # data.to_csv('./10_21_6/dqn/collect_compute.csv', index=False)
    data.to_csv('./no_offload/10_21_6/dqn/collect_computeha.csv', index=False)
    # data.to_csv('./poisson/10_21_6/greedy/collect_compute.csv', index=False)
