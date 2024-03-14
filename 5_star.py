import networkx as nx
import random as random
from eulerian import path
from star_graph import n_star

G = n_star(5)
count = 0
path_lengths = nx.all_pairs_shortest_path_length(G)
path_lengths_dict = {(u, v): d for u, paths in path_lengths for v, d in paths.items()}
path_lengths_list = list(path_lengths_dict.items())
random.shuffle(path_lengths_list)
path_lengths_dict_shuffled = dict(path_lengths_list)
sorted_pairs = sorted(path_lengths_dict_shuffled.items(), key=lambda item: item[1], reverse=True)
K = nx.DiGraph(G)
for (u, v), d in sorted_pairs:
    P = path(K, u, v)
    print(count, nx.diameter(K), len(P)-1, nx.is_eulerian(K))
    count += 1
    # for i in range(len(P) - 1):
    #     if (P[i+1], P[i]) in K.edges():
    #         K.remove_edge(P[i+1], P[i])
    if nx.number_of_edges(K) <= nx.number_of_edges(G):
        break

print(count)
print(nx.diameter(K))