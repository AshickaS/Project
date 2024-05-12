import networkx as nx
import time
import eulerian
from star_graph import n_star

n = 5
test_number = 100

orientation = eulerian.maximum_distance_pair_orientation	#Algorithm 1
#orientation = eulerian.random_walk_orientation				#Algorithm 2
#orientation = eulerian.random_walk_orientation_new			#Algorithm 3
#orientation = eulerian.eulerian_orientation_with_cycles	#Algorithm 4
#orientation = eulerian.initial_max_cycle_orientation		#Algorithm 5
#orientation = eulerian.all_pairs_max_cycle_orientation		#Algorithm 6
#orientation = eulerian.max_cycle_orientation				#Algorithm 7
#orientation = eulerian.random_pair_max_dist_orientation	#Algorithm 8

G = n_star(n)
diameters = []
time_taken = 0

for i in range(test_number):
	t1 = time.time()
	K = orientation(G)
	t2 = time.time()
	time_taken += t2-t1
	diameters.append(nx.diameter(K))

minimum = min(diameters)
minimum_count = diameters.count(minimum)
time_per_test = time_taken/test_number

print('The minimum diameter obtained is', minimum)
print('The number of times the diameter',minimum,
	'was obtained is', minimum_count,'out of',test_number)
print('Time taken for', orientation.__name__, 'method is',time_per_test)