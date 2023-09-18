import networkx as nx
import random

def eulerian_circuit(G):
    D = G.copy()
    DG = nx.DiGraph() 
    DG.add_nodes_from(G)
    V = list(G.nodes())
    while D.number_of_edges() > 0:
        v = random.choice(V)
        while True:
            #print(v)
            N = list(D.neighbors(v))
            if len(N) == 0:
                break
            u = random.choice(N)
            DG.add_edge(v, u)
            D.remove_edge(v, u)
            v = u
    return DG
 

