from graph import Graph, DGraph
import random

def GenRandomGraph(n,min_weight,max_weight):
	for i in range(n):
		for j in range(n):
			if i != j:
				w = random.randint(min_weight,max_weight)
				D.add(i,j,w)


def VC(i):
	global Config
	global MIN_CAMERAS
	global BC
	if i == N-1:
		if not Promising():
			return
		min_cam = len([x for x in Config if x])
		if min_cam < MIN_CAMERAS:
			BC = Config.copy()
			MIN_CAMERAS = min_cam
	else:
		Config[i+1] = False
		VC(i+1)
		Config[i+1] = True
		VC(i+1)
def Promising():
	global Config
	edges = D.Edges.copy()
	for i in range(N):
		if Config[i]:
			for e in D.Edges:
				if (e[0] == i or e[1] == i) and e in edges:
					del edges[e]
	return len(edges) == 0
N = 4
D = DGraph()
GenRandomGraph(N,1,100)
Config = [None]*N
MIN_CAMERAS = N
BC = []
VC(-1)
print(MIN_CAMERAS)