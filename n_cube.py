import networkx as nx
import itertools
import matplotlib.pyplot as plt
import time
import functions
import numpy as np 

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
	f = open(f'matrix1_n{n}.txt', 'w')
	print(C, file = f)	
	final_time = time.time()
	time_taken  = final_time - initial_time
	print('Time1 =', time_taken)	

def n_cube2(n):
	initial_time = time.time()
	group =[np.array(p) for p in itertools.product(range(2), repeat = n)]
	generator_list = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
	generators = [np.array(l) for l in generator_list]
	G = nx.DiGraph()
	G.add_nodes_from([tuple(i) for i in group])
	for generator in generators:
		for tail in G.nodes:
			head = (tail + generator) % 2
			G.add_edge(tuple(tail), tuple(head))
	G = functions.to_undirected(G)
	A = nx.adjacency_matrix(G)
	B = A.todense()
	C = '\n'.join([' '.join([str(x) for x in row]) for row in B])
	f = open(f'matrix2_n{n}.txt', 'w')
	print(C, file = f)
	final_time = time.time()
	time_taken  = final_time - initial_time
	print('Time2 =', time_taken)

