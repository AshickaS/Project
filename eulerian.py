'''
This program calculates the minimum diameter of n-cube by its eulerian orientation.
'''
import networkx as nx
import random
from n_cube import n_cube2

'''
The function eulerian_orientation() takes as input a graph G and returns an oriented digraph DG. 
'''
def eulerian_orientation(G):
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
    return DG
'''
The function eulerian orientation2() finds a cycle in G and orients it by a coin toss experiment. The remaining edges are randomly oriented.
'''
def eulerian_orientation2(G):
    D = G.copy()
    DG = nx.DiGraph()
    DG.add_nodes_from(G)
    C = nx.find_cycle(G)
    if random.randint(0,1) == 1:
        for edge in C:    
            DG.add_edge(edge[0], edge[1])
    else:
        for edge in C:
            DG.add_edge(edge[1], edge[0])
    D.remove_edges_from(C)
    for edge in D.edges:
        if random.randint(0,1) == 0:
            DG.add_edge(edge[0], edge[1])
        else:
            DG.add_edge(edge[1], edge[0])
    return DG
'''
The function minimum_diameter() calls the function eulerian_orientation() sample_size many times for the graph G, stores the corresponding diameters in a set and returns the minimum. 
'''
def minimum_diameter(G, sample_size):
    diameters = set()
    for i in range(sample_size):
        diameter = nx.diameter(eulerian_orientation(G))      #calculate the diameter sample size many timess
        diameters.add(diameter)     #store the diameters
    return min(diameters)       #return the minimum diameter

G = n_cube2(4)
sample_size = 100
print(minimum_diameter(G, sample_size))

 

