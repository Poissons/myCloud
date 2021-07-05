import json
import os

master_name = 'master'
update_interval = 3
tasks_execute_situation_on_each_node_dict = {
    "master": {"4": {"success": 1, "failure": 0}, "11": {"success": 0, "failure": 1},
               "8": {"success": 1, "failure": 0}}}
current_service_on_each_node_dict = {"master": {"node1": {"4": 2, "11": 1}, "node2": {"8": 2}}}
stuck_tasks_situation_on_each_node_dict = {
    "master": {"4": {"stuck": 1}, "11": {"stuck": 1}, "8": {"stuck": 1}, "6": {"stuck": 1}, "2": {"stuck": 1},
               "1": {"stuck": 2}}}
resources_on_each_node_dict = {"master": {
    'node1': {'memory': {'percent': '13', 'number': '2098Mi'}, 'storage': {'percent': '3', 'number': '4Gi'},
              'cpu': {'percent': '2', 'number': '100m'}},
    'node2': {'memory': {'percent': '13', 'number': '2098Mi'}, 'storage': {'percent': '3', 'number': '4Gi'},
              'cpu': {'percent': '2', 'number': '100m'}}}}
epoch_index = 2

observation = json.dumps([master_name, update_interval, tasks_execute_situation_on_each_node_dict,
                          current_service_on_each_node_dict,
                          stuck_tasks_situation_on_each_node_dict, resources_on_each_node_dict,
                          epoch_index])

print(observation)
# ["master", 3, {"master": {"4": {"success": 1, "failure": 0}, "11": {"success": 0, "failure": 1}, "8": {"success": 1, "failure": 0}}}, {"master": {"node1": {"4": 2, "11": 1}, "node2": {"8": 2}}}, {"master": {"2": {"stuck": 1}, "6": {"stuck": 1}, "4": {"stuck": 1}, "11": {"stuck": 1}, "1": {"stuck": 2}, "8": {"stuck": 1}}}, {"master": {"node1": {"memory": {"percent": "13", "number": "2098Mi"}, "storage": {"percent": "3", "number": "4Gi"}, "cpu": {"percent": "2", "number": "100m"}}, "node2": {"memory": {"percent": "13", "number": "2098Mi"}, "storage": {"percent": "3", "number": "4Gi"}, "cpu": {"percent": "2", "number": "100m"}}}}, 2]

# result = os.popen(
#         'curl http://localhost:4001/predict -X POST -d \'observation=' + observation + '\''
#     ).read()
#
# result = json.loads(result)
# print(result)
