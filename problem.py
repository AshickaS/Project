import networkx as nx 
import numpy as np
from tabulate import tabulate
import random

def minimum_diameter(G, sample_size, n1, n2):       #n1 denotes n value in n_cube, n2 denotes function number of n_cube1 or n_cube2  
    m = G.number_of_edges()     #size of the graph
    f = open(f'output{n2}_{n1}.txt', 'w')
    F = nx.adjacency_matrix(G)      #create the adjacency matrix
    K = F.toarray()
    print(f'Input graph:\n\n {K}',file = f)         #print the input graph to the file
    print(f'The diameter of the input graph is {nx.diameter(G)}', file = f) 		#print the diameter
    min_diameter = float('inf')       #initialize the minimum diameter as infinity
    min_vector = None       #vector corresponding to minimum diameter
    min_digraph = None      #digraph corresponding to minimum diameter
    result = []
    bit_vector_sample = []      #create a sample of bit vectors
    for i in range (sample_size):
        v = [0] * m
        for j in range (len(v)):
            v[j] = random.randint(0,1)
        bit_vector_sample.append(tuple(v))
    for vector in bit_vector_sample:
        DG = nx.DiGraph() 		#create a digraph for each vector
        DG.add_nodes_from(G)
        for edge, bit in zip(G.edges(), vector): 		#orient the graph
        #    print(edge, bit)
            if bit == 0:
                DG.add_edge(edge[0], edge[1])
            else:
                DG.add_edge(edge[1], edge[0])
        A = nx.adjacency_matrix(DG)
        digraph = A.toarray()
        if nx.is_strongly_connected(DG):        #calculate the diameter
            diameter = nx.diameter(DG)
            if diameter < min_diameter:         #compare the diameters and update the result
                min_diameter = diameter
                min_vector = vector
                min_digraph = digraph 
                result.append((min_vector, min_digraph, min_diameter)) 	
    if len(result) == 0:         #find the minimum
        print('\nAll the diameters are infinity', file = f)	    
    else:
        print(tabulate(result, headers=['Vector', 'Digraph', 'Diameter'], tablefmt = 'grid'), file = f)       #print the result
        print(f'\nMinimum among the diameters is {min_diameter}', file = f)

