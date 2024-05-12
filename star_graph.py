import networkx as nx
import itertools
import relabel
import random
from sympy.combinatorics.permutations import Permutation
from eulerian import eulerian_orientation_with_cycles


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

def oriented_n_star(n):
	'''
	The function oriented_n_star() uses the function eulerian_orientation_with_cycles() to generate an oriented n-star by recursion.
	'''
	G = nx.DiGraph()
	labels = 'abcdefghijklmnopqrstuvwxyz'
	if n == 1:
		G.add_node(labels[0])
		return G
	
	if n == 4:
		nodes = [''.join(p) for p in itertools.permutations(labels[:4], 4)]
		G.add_nodes_from(nodes)
		signature = dict()
		for node in G.nodes:
			per = [ord(i) - ord('a') for i in node] 
			sgn = Permutation(per).signature()
			signature[node] = sgn
		for node in G.nodes:
			if signature[node] == 1:
				nbr1 = node[1] + node[0] + node[2:]
				nbr2 = node[-2::-1] + node[-1]
				if nbr1 in G.nodes:
					G.add_edge(node, nbr1)
				if nbr2 in G.nodes:
					G.add_edge(node, nbr2)
			else:
				nbr = node[-1] + node[1:-1] + node[0]
				if nbr in G.nodes:
					G.add_edge(node, nbr)
		return G 

	G_prev = oriented_n_star(n - 2)
	G_copies = [G_prev.copy() for i in range (n*(n - 1))]
	for G in G_copies:
		if(random.randint(0,1) == 1):
			G.reverse()
	s1_list = [list(G_prev.nodes) for G_prev in G_copies]
	s2_list = [''.join(p) for p in itertools.permutations(labels[:n], 2)]
	relabeled_copies = [nx.relabel_nodes(G_copy,
					dict(zip(s1, relabel.bulk_relabel(s1, s2)))) \
					for G_copy, s1, s2 in zip(G_copies, s1_list, s2_list)]
	
	G = nx.union_all(relabeled_copies)
	H = nx.Graph()
	H.add_nodes_from(list(G.nodes()))
	for node1 in H.nodes():
		nbr1 = list(node1)
		nbr1[0] = node1[-2]
		nbr1[-2] = node1[0]
		nbr1_str = ''.join(i for i in nbr1)
		H.add_edge(node1, nbr1_str)
		
		nbr2 = list(node1)
		nbr2[0] = node1[-1]
		nbr2[-1] = node1[0]
		nbr2_str = ''.join(i for i in nbr2)
		H.add_edge(node1, nbr2_str)
	
	H_orient = eulerian_orientation_with_cycles(H)
	K = nx.compose(G, H_orient)
	return K