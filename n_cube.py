import networkx as nx
import itertools
import matplotlib.pyplot as plt

def n_cube(n):
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
		flag = True
		for u,v in G.edges:
			if not G.has_edge(v,u):
				flag = False
				break
		if flag:
			G = G.to_undirected()
	A = nx.adjacency_matrix(G)
	B = A.todense()
	C = '\n'.join([' '.join([str(x) for x in row]) for row in B])
	f = open('matrix.txt', 'w')
	print(C, file = f)		

n_cube(3)		