import networkx as nx
import random

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

def path(DG, s, t):
    '''
    The function path() takes as input a graph DG and two vertices s and t. It
    checks if the shortest path length from s to t is greater than 1000, and
    if so, returns an empty list. Otherwise, it finds the shortest path from s 
    to t, orients the edges of DG in this direction, assigns them weight and
    finds the shortest path from t to s in the updated graph and orients the
    edges of DG in the direction of this new path. The function returns the
    combined path.
    '''
    if nx.shortest_path_length(DG, s, t, weight='weight') > 1000:
        return []
    p1 = nx.dijkstra_path(DG, s, t)
    for i in range(len(p1) - 1):
        if ((p1[i+1],p1[i]) in DG.edges()):
            DG.remove_edge(p1[i+1], p1[i])
            DG[p1[i]][p1[i+1]]['weight'] = 1000
    p2 = nx.dijkstra_path(DG, t, s)
    for i in range(len(p2) - 1):
        if (p2[i+1], p2[i]) in DG.edges():
            DG.remove_edge(p2[i+1], p2[i])
            DG[p2[i]][p2[i+1]]['weight'] = 1000
    return p1+p2[1:]

def approximate_diameter(G, sample_size):
    '''
    The function approximate_diameter() calculates the eccentricites of a random sample of vertices and returns their maximum.
    '''
    V = list(G.nodes())
    sample_nodes = random.sample(V, sample_size)
    eccentricities = nx.eccentricity(G, sample_nodes)
    diameter = max(eccentricities.values())
    return diameter