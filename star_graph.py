import networkx as nx
import itertools

def n_star(n):
	'''
	The function n_star() takes as argument n, generates and returns an n-star graph.
	'''
	G = nx.Graph()
	labels = 'abcdefghijklmnopqrstuvwxyz'
	nodes = list(itertools.permutations(labels[:n]))
	G.add_nodes_from(nodes)
	for node1 in nodes:
		for node2 in nodes:
			diff_positions = [i for i in range (n) if node1[i] != node2[i]]
			if len(diff_positions) == 2 and diff_positions[0] == 0:
				G.add_edge(node1, node2)
	return G