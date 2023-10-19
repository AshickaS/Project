'''
This program calculates the minimum diameter of n-cube by its eulerian orientation.
'''
import networkx as nx
import random
from n_cube import n_cube2

def random_walk_orientation(G):
    '''
    The function random_walk_orientation() takes as input a graph G and returns an oriented digraph DG. 
    '''
    D = G.copy()        #remove the edges from this graph
    DG = nx.DiGraph()       #add the edges to this graph 
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

def eulerian_orientation_with_cycles(G):
    '''
    The function eulerian_orientation_with_cycles() finds the cycles in G and orient their edges by a coin toss experiment. The remaining edges are oriented randomly.
    '''
    D = G.copy()        
    DG = nx.DiGraph()      
    V = list(G.nodes())     
    while True:
        try:
            nx.find_cycle(D)
        except nx.exception.NetworkXNoCycle as e:
            for edge in D.edges:        
                if random.randint(0,1) == 0:
                    DG.add_edge(edge[0], edge[1])
                else:
                    DG.add_edge(edge[1], edge[0])
            return DG           
        while True:
            v = random.choice(V)        
            try:
                C = nx.find_cycle(D,v)
            except nx.exception.NetworkXNoCycle as e:
                continue    
            break    
        toss = random.randint(0,1)
        if toss:
            for edge in C:     
                DG.add_edge(edge[0], edge[1])
                D.remove_edge(edge[0], edge[1])
        else:
            for edge in C:     
                DG.add_edge(edge[1], edge[0])
                D.remove_edge(edge[0], edge[1])

def maximum_matching_orientation(G):
    '''
    The function maximum_matching_orientation() finds a maximum matching M of the graph G and orients the edges in M randomly. Then it finds the cycles in G and orient their edges. 
    '''
    M = nx.algorithms.bipartite.maximum_matching(G)
    DG = nx.DiGraph()
    D1 = G.copy()
    D2 = nx.Graph()
    V = list(G.nodes())
    n = G.degree(V[0])
    if n % 2 == 0:
        return None
    for key, value in M.items():
        D2.add_edge(key, value)
    for edge in D2.edges:
        if random.randint(0,1) == 0:
            DG.add_edge(edge[0], edge[1])
        else:
            DG.add_edge(edge[1], edge[0])
        D1.remove_edge(edge[0], edge[1])
    while True:
        try:
            nx.find_cycle(D1)
        except nx.exception.NetworkXNoCycle as e:
            return DG       
        while True:
            v = random.choice(V)        
            try:
                C = nx.find_cycle(D1,v)
            except nx.exception.NetworkXNoCycle as e:
                continue    
            break    
        toss = random.randint(0,1)
        if toss:
            for edge in C:     
                DG.add_edge(edge[0], edge[1])
                D1.remove_edge(edge[0], edge[1])
        else:
            for edge in C:     
                DG.add_edge(edge[1], edge[0])
                D1.remove_edge(edge[0], edge[1])

def minimum_diameter(G, sample_size, orientation):
    '''
    The function minimum_diameter() calls the function orientation sample_size many times for the graph G, stores the corresponding diameters in a set and returns the minimum. 
    '''
    diameters = set()
    K = orientation(G)
    if K != None:
        for i in range(sample_size):
            diameter = nx.diameter(K)      #calculate the diameter sample size many times
            diameters.add(diameter)     #store the diameters
        return min(diameters)       #return the minimum diameter

G = n_cube2(4)
sample_size = 100
orientation = maximum_matching_orientation
print(minimum_diameter(G, sample_size, orientation))

 

