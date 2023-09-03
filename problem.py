import networkx as nx 
import numpy as np
import itertools
from tabulate import tabulate
import random

def minimum_diameter(input_file, sample_size): 
    input_graph = np.loadtxt(input_file)      #load the input file
    G = nx.Graph(input_graph)         #create a graph
    m = G.number_of_edges()     #size of the graph
    n = G.number_of_nodes() 	#order of the graph
    f = open('output.txt', 'w')
    F = nx.adjacency_matrix(G)      #create the adjacency matrix
    K = F.toarray()
    print(f'Input graph:\n\n {K}',file = f)         #print the input graph to the file
    print(f'The diameter of the input graph is {nx.diameter(G)}', file = f) 		#print the diameter
    diameters = []      #create a list for diameters
    result = []
    bit_vector_list = list(itertools.product(range(2), repeat=m))         #create a list of bit vectors
    bit_vector_sample = random.sample(bit_vector_list, sample_size)         #create a random sample of bit vectors    
    for vector in bit_vector_sample:
        DG = nx.DiGraph() 		#create a digraph for each vector
        DG.add_nodes_from([i for i in range (n)])
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
            diameters.append(diameter)
        else:
            diameter = 'infinity' 
        result.append((vector, digraph, diameter)) 		
    print(tabulate(result, headers=['Vector', 'Digraph', 'Diameter'], tablefmt = 'grid'), file = f)         #print the result
    if len(diameters) == 0:         #find the minimum
        print('\nAll the diameters are infinity', file = f)
    else:
        print(f'\nMinimum among the diameters is {min(diameters)}', file = f)

minimum_diameter('input3.txt', 100)