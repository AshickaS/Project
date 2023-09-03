def is_undirected(G):
	for u, v in G.edges:
		if not G.has_edge(v, u):
			return False
	return True

def to_undirected(G):
	if is_undirected(G):
		G = G.to_undirected()
		return G