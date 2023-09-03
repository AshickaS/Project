import networkx as nx
import itertools
import matplotlib.pyplot as plt
import time
import functions

def n_cube1(n):
	initial_time = time.time()
	group = [''.join(map(str, p)) for p in itertools.product(range(2), repeat = n)]
	generators = ['0' * i + '1' + '0' * (n - i - 1) for i in range(n)]
	G = nx.DiGraph()
	G.add_nodes_from(group)
	for generator in generators:	
		for tail in G.nodes:
			head = ''
			for i in range(n):
				head += str((int(tail[i]) + int(generator[i])) % 2)		
			G.add_edge(tail, head)
	G = functions.to_undirected(G)	
	A = nx.adjacency_matrix(G)
	B = A.todense()
	C = '\n'.join([' '.join([str(x) for x in row]) for row in B])
	f = open('matrix.txt', 'w')
	print(C, file = f)	
	final_time = time.time()
	time_taken  = final_time - initial_time
	print('Time1 =', time_taken)	

n_cube1(3)		