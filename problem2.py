import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

def cayley_graph(n):
	group = [i for i in range (n)]
	generating_set = [[i, (n - i)%n] for i in range((n//2)+1)]
	result = []
	f = open('out2_0.txt', 'w')
	print(f'The order of the group is {n}', file = f)
	for generator in generating_set:
		G = nx.DiGraph()
		G.add_nodes_from(group)
		for g in generator:
			for v in G.nodes:
				G.add_edge(v, (v + g) % n)
		nodes = list(G.nodes)
		for u in nodes:
			for v in nodes:
				if G.has_edge(u,v) and G.has_edge(v,u):
					G = G.to_undirected()
		A = nx.adjacency_matrix(G)
		B = A.toarray()
		result.append((generator, B))
	print(tabulate(result, headers=['Generator', 'Graph'], tablefmt="grid"), file = f)
	
cayley_graph(5)