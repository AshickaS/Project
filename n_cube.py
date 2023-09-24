import networkx as nx
import itertools
import matplotlib.pyplot as plt
import time
import functions
import numpy as np 

def n_cube1(n):
	initial_time = time.time()		#calculate the initial time
	group = [''.join(map(str, p)) for p in itertools.product(range(2), repeat = n)]		#create the group
	generators = ['0' * i + '1' + '0' * (n - i - 1) for i in range(n)]		#create a list of generators
	G = nx.DiGraph()		#create the digraph
	G.add_nodes_from(group)		#add the nodes from the group to G
	for generator in generators:		#orient the graph	
		for tail in G.nodes:
			head = ''
			for i in range(n):
				head += str((int(tail[i]) + int(generator[i])) % 2)		
			G.add_edge(tail, head)
	G = functions.to_undirected(G)		#check if the graph is undirected and if so make it undirected	
	final_time = time.time()		#calculate the final time
	time_taken  = final_time - initial_time		#calculate the total time
	print('Time1 =', time_taken)		#print the time
	return G		#return the graph	

def n_cube2(n):
	initial_time = time.time()		#calculate the initial time	
	group =[np.array(p) for p in itertools.product(range(2), repeat = n)]		#create the group		
	generator_list = [[1 if i == j else 0 for j in range(n)] for i in range(n)]		#create a list of generators
	generators = [np.array(l) for l in generator_list]		#create a list of generators of numpy arrays
	G = nx.DiGraph()		#create the digraph
	G.add_nodes_from([tuple(i) for i in group])		#add the nodes from the group to G as tuples
	for generator in generators:		#orient the graph
		for tail in G.nodes:
			head = (tail + generator) % 2
			G.add_edge(tuple(tail), tuple(head))
	G = functions.to_undirected(G)		#check if the graph is undirected and if so make it undirected
	final_time = time.time()		#calculate the final time
	time_taken  = final_time - initial_time		#calculate the total time
	print('Time2 =', time_taken)		#print the time
	return G		#return the graph
