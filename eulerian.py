import networkx as nx
import random
import itertools

def random_walk_orientation(G):
    '''
    The function random_walk_orientation() takes as input a graph G orients
    the edges randomly and returns an oriented digraph DG of G. 
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

def random_walk_orientation_new(G):
    '''
    The function random_walk_orientation_new() takes as input a graph G and
    orients the edges by selecting a random walk prefering the non visited
    vertices. The function returns an oriented graph of G.
    '''
    D = G.copy()        #remove the edges from this graph
    DG = nx.DiGraph()       #add the edges to this graph 
    DG.add_nodes_from(G)
    V = list(G.nodes())     #vertex set of G
    visited = {v: False for v in V}     #dictionary to keep track of visited vertices
    while D.number_of_edges() > 0:
        v = random.choice(V)        #select a random vertex in G
        visited[v] = True
        while True:
            N = [u for u in D.neighbors(v) if not visited[u]]        #N(v) excluding visited vertices
            if len(N) == 0:     #if N(v) is empty, select from visited vertices
                N = list(D.neighbors(v))
                if len(N) == 0:     #break the loop if N(v) is still empty
                    break
            u = random.choice(N)        #select a random neighbour of v
            visited[u] = True
            DG.add_edge(v, u)       #add edge to resultant digraph DG
            D.remove_edge(v, u)     #remove the edge from D
            v = u       #repeat the process at u
    return DG

def eulerian_orientation_with_cycles(G):
    '''
    The function eulerian_orientation_with_cycles() finds the cycles in G and
    orient their edges by a coin toss experiment. The remaining edges are
    oriented randomly.
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
    The function maximum_matching_orientation() finds a maximum matching M of
    the graph G and orients the edges in M randomly. Then it finds the cycles
    in G and orient their edges. 
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

def maximum_distance_pair_orientation(G):
    '''
    The maximum_distance_pair_orientation() takes as input a graph and orients
    the edges between two pairs of vertices selected randomly in the direction
    of longer path between these two vertices. The function returns the final 
    oriented graph.
    '''
    K = nx.DiGraph(G)
    V = list(G.nodes())
    pairs = list(itertools.combinations(V,2))
    random.shuffle(pairs)
    for u,v in pairs:
        ori_path = max_dist_pair_path(K, u, v)
		#print(nx.diameter(K),nx.number_of_edges(K), nx.is_eulerian(K))
        if nx.number_of_edges(K) == nx.number_of_edges(G):
            return K

def initial_max_cycle_orientation(G):
    '''
    The function initial_max_cycle_orientation() takes as input a graph G and
    creates a dictionary of vertex pair and their distances. The dictionary is
    shuffled and sorted in non increasing order of distances. The edges are
    oriented taking the pair of vertices from the dictionary as defined by the
    path() function. The function returns the oriented graph of G.
    '''
    count = 0
    path_lengths = nx.all_pairs_shortest_path_length(G)
    path_lengths_dict = {(u, v): d for u, paths in path_lengths \
                                for v, d in paths.items()}
    path_lengths_list = list(path_lengths_dict.items())
    random.shuffle(path_lengths_list)
    path_lengths_dict_shuffled = dict(path_lengths_list)
    sorted_pairs = sorted(path_lengths_dict_shuffled.items(), 
                          key=lambda item: item[1], reverse=True)
    K = nx.DiGraph(G)
    for (u, v), d in sorted_pairs:
        P = path(K, u, v)
        #print(count, nx.diameter(K), len(P)-1, nx.is_eulerian(K))
        count += 1
        if nx.number_of_edges(K) <= nx.number_of_edges(G):
            return K

def max_dist_pair_path(DG,s,t):
    '''
    The function max_dist_pair_path() takes as input a graph DG and two
    vertices s and t and orients the edges from either s to t or from t to s
    according as which one is longer. The function returns the desired path. 
    '''
    st_path = nx.shortest_path(DG,s,t)
    ts_path = nx.shortest_path(DG,t,s)
    if len(st_path) > len(ts_path):
        for i in range(len(st_path) - 1):
            if ((st_path[i+1],st_path[i]) in DG.edges()):
                DG.remove_edge(st_path[i+1], st_path[i])
        return st_path
    else:
        for i in range(len(ts_path) - 1):
            if ((ts_path[i+1],ts_path[i]) in DG.edges()):
                DG.remove_edge(ts_path[i+1], ts_path[i])
        return ts_path

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