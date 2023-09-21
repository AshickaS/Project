import networkx as nx
import random
from n_cube import n_cube2

def eulerian_circuit(G):
    D = G.copy()        #remove the vertices from this graph
    DG = nx.DiGraph()       #add the vertices to this graph 
    DG.add_nodes_from(G)
    V = list(G.nodes())     #vertex set of G
    while D.number_of_edges() > 0:
        v = random.choice(V)        #select a random vertex in G
        while True:
            #print(v)
            N = list(D.neighbors(v))        #N(v)
            if len(N) == 0:     #break the loop if N(v) is empty
                break
            u = random.choice(N)        #select a random neighbour of v
            DG.add_edge(v, u)       #add edge to resultant digraph DG
            D.remove_edge(v, u)     #remove the edge from D
            v = u       #repeat the process at u
    return nx.diameter(DG)

def minimum_diameter(G, sample_size):
    diameters = set()
    for i in range(sample_size):
        diameter = eulerian_circuit(G)      #calculate the diameter sample size many timess
        diameters.add(diameter)     #store the diameters
    return min(diameters)       #return the minimum diameter

G = n_cube2(4)
sample_size = 100
print(minimum_diameter(G, sample_size))

 

