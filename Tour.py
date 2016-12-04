from graph import Graph, DGraph
import random


def GenRandomGraph(n,min_weight,max_weight):
	for i in range(n):
		for j in range(n):
			if i != j:
				w = random.randint(min_weight,max_weight)
				D.add(i,j,w)

def Tour(i):
	global BC
	global min_dis
	if not Promising(i):
		return
	if i == N-1:
		if (Config[N-1],Config[0]) in D: 
			d = Distance()
			if min_dis >= d:
				BC = Config.copy()
				min_dis = d
	else:
		for j in range(N):
			if j not in Config[0:i+1]:
				Config[i+1] = j
				Tour(i+1)

def Distance():
	global min_dis
	if N < 2:
		return 0
	distance = D[Config[N-1],Config[0]]
	for i in range(1,N):
		distance = distance + D[Config[i-1],Config[i]]
	if min_dis == None:
		min_dis = distance
	return distance

def Promising(i):
	global Config
	if i < 1:
		return True
	u,v = Config[i-1],Config[i]
	return (u,v) in D

N = 5
Config = [None]*N
D = DGraph()
GenRandomGraph(N,1,50)
min_dis = None
BC = []
Tour(-1)
print("Best tour :",BC)
print("min distance :",min_dis)
