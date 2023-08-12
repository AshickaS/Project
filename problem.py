import networkx as nx 
import numpy as np
import itertools

AdjacencyMatrix = np.loadtxt('input1.txt')      #load the input file
G = nx.Graph(AdjacencyMatrix)         #create a graph
m = G.number_of_edges()     #size of the graph
n = G.number_of_nodes() 	#order of the graph
f = open('output1.txt', 'w')
print(f'The diameter of the input graph is {nx.diameter(G)}', file = f) 		#print the diameter
diameters = []      #create a list for diameters
BitVectorList = list(itertools.product(range(2), repeat=m))         #create a list of bit vectors
for vector in BitVectorList:
    DG = nx.DiGraph() 		#create a digraph for each vector
    for edge, bit in zip(G.edges(), vector): 		#orient the graph
    #    print(edge, bit)
        if bit == 0:
            DG.add_edge(edge[0], edge[1])
        else:
            DG.add_edge(edge[1], edge[0])
    Digraph = np.array([[0] * n for i in range(n)]) 		#create the adjacency matrices for the digraphs
    for edge in DG.out_edges():
        Digraph[edge[0]][edge[1]] = 1
    #A = nx.adjacency_matrix(DG)
    #Digraph = A.toarray()
    if nx.is_strongly_connected(DG):        #calculate the diameter
        diameter = nx.diameter(DG)
        diameters.append(diameter)
    else:
        diameter = 'infinity' 
    print(f'\n({Digraph}, {diameter})', file = f) 		#print the digraph-diameter pair
if len(diameters) == 0:         #find the minimum
    print('\nAll the diameters are infinity', file = f)
else:
    print(f'\nMinimum among the diameters is {min(diameters)}', file = f)