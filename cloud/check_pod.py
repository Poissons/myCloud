# -*- coding: utf-8 -*- 
import os 

class Pod(object):
	def __init__(self, name, ready, status, restarts, age, ip, node):
		self.name = name
		self.ready = ready
		self.status = status
		self.restarts = restarts
		self.age = age
		self.ip = ip
		self.node = node


# 输入：pod关键字
# 输出：属性完善的pod类
# 作用：获取pod当前状态
def check_pod(target):
	pods = os.popen('kubectl get pod -o wide').read()
	#index = pods.find(target)
	index = 0	
	index_list =[]

	while pods.find(target,index) !=  -1:
		if pods.find(target,index) != len(pods)-1:
			print("!",pods.find(target,index))
			index_list.append(pods.find(target,index))
			index = pods.find(target,index) + 1
		else: 
			index = pods.find(target,index)
			break

	print(index_list)
	#	while pods.find(target,index) !=  -1:
	#		index_list.append(pods.find(target,index))
	#		index = pods.find(target,index) + 1
	#		#print(pods.find(target,index))
	#	#print(index_list)
	
	pod_list = []
	for i in range(len(index_list)):
		target_pod = Pod('','','','','','','')
		index = index_list[i]
		while pods[index] != ' ':
			target_pod.name = target_pod.name + pods[index]
			index = index + 1
		while pods[index] == ' ':
			index = index + 1

		while pods[index] != ' ':
			target_pod.ready = target_pod.ready + pods[index]
			index = index + 1
		while pods[index] == ' ':
			index = index + 1

		while pods[index] != ' ':
			target_pod.status = target_pod.status + pods[index]
			index = index + 1
		while pods[index] == ' ':
			index = index + 1
	
		while pods[index] != ' ':
			target_pod.restarts = target_pod.restarts + pods[index]
			index = index + 1
		while pods[index] == ' ':
			index = index + 1
	
		while pods[index] != ' ':
			target_pod.age = target_pod.age + pods[index]
			index = index + 1
		while pods[index] == ' ':
			index = index + 1
	
		while pods[index] != ' ':
			target_pod.ip = target_pod.ip + pods[index]
			index = index + 1
		while pods[index] == ' ':
			index = index + 1
	
		while pods[index] != ' ':
			target_pod.node = target_pod.node + pods[index]
			index = index + 1
		while pods[index] == ' ':
			index = index + 1

		if target_pod.status == 'Running':
			pod_list.append(target_pod)
		#print(target_pod.status,'!')
	return pod_list

if __name__ == '__main__':
	target = '\n'
	target_pod = check_pod(target)
	for pod in target_pod:
		print(f'[{pod.name.lstrip()}]')
		print(pod.ready)
		print(pod.status)
		print(pod.node)

