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
    D = G.copy()        #remove the edges from this graph
    DG = nx.DiGraph()       #add the edges to this graph 
    DG.add_nodes_from(G)
    V = list(G.nodes())     #vertex set of G

    while D.number_of_edges() > 0:
        v = random.choice(V)        #select a random vertex in G
        if (not nx.find_cycle(D, v)):
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
The function eulerian_orientation1() randomly selects a vertex v and checks for a ciruit starting and ending at v. 
The vertices along the ciruit are stored in a list C and the edges corresponding to them are oriented in the resultant graph DG. 
The remaiming edges are oriented randomly.
'''
def eulerian_orientation1(G):
    D = G.copy()        #remove edges from this graph
    DG = nx.DiGraph()       #add edges to this graph
    V = list(G.nodes())     #V(G)
    #print(v)
    num_cycles = 0

    while True:
        try:
            nx.find_cycle(D)
        except nx.exception.NetworkXNoCycle as e:
            print("Found the no cycle exception after finding", num_cycles, " cycles")
            print("Number of remaining edges = ", D.number_of_edges())
            for edge in D.edges:        #orient the remaining edges randomly
                if random.randint(0,1) == 0:
                    DG.add_edge(edge[0], edge[1])
                else:
                    DG.add_edge(edge[1], edge[0])
            return DG       #return the oriented graph
        
        while True:
            v = random.choice(V)        #select a random vertex
            try:
                C = nx.find_cycle(D,v)
            except nx.exception.NetworkXNoCycle as e:
                print("No cycles from the chosen vertex")
                continue    
            print("A vertex with a cycle found")
            break

        num_cycles += 1
        print("A cycle of length ", len(C), " found.")    
        toss = random.randint(0,1)
        if toss:
            for e in C:     #orient the edges of the circuit
                DG.add_edge(e[0], e[1])
                D.remove_edge(e[0], e[1])
        else:
            for e in C:     #orient the edges of the circuit
                DG.add_edge(e[1], e[0])
                D.remove_edge(e[0], e[1])
    
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
        D = eulerian_orientation1(G)
        if nx.is_strongly_connected(D):
            diameter = nx.diameter(D)      #calculate the diameter sample size many timess
            diameters.add(diameter)     #store the diameters
    return min(diameters)       #return the minimum diameter

G = n_cube2(5)
sample_size = 3
print(minimum_diameter(G, sample_size))

 

