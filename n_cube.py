import networkx as nx
import itertools
import matplotlib.pyplot as plt

def n_cube(n):
	group = list(itertools.product(range(2), repeat=n))
	generators = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
	G = nx.DiGraph()
	G.add_nodes_from(group)
	for generator in generators:	
		for tail in G.nodes:
			head = [0]*n
			for i in range(n):
				head[i] = (tail[i] + generator[i])%2
			G.add_edge(tuple(tail), tuple(head))
		flag = True
		for u,v in G.edges:
			if not G.has_edge(v,u):
				flag = False
				break
		if flag:
			G = G.to_undirected()
	nx.draw(G, with_labels = True)
	plt.show()
n_cube(3)		