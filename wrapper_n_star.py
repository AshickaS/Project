import networkx as nx 
import star_graph
import eulerian
import time

n = 6
sample_size = 25
orientation = eulerian.maximum_matching_orientation # set the orientation among eulerian.random_walk_orientation, eulerian.eulerian_orientation_with_cycles, eulerian.maximum_matching_orientation, None(for recursive orientation)
sample_vertex_size = 25 #for approximate diameter

diameters = []
orientation_time = []
diameter_time = []


if orientation != None:
	t1 = time.time()
	G = star_graph.n_star(n)
	t2 = time.time()
	
	t_c = t2 - t1
	print('Construction time is', t_c)
	
	for i in range (sample_size):
		t1 = time.time()
		K = orientation(G)
		t2 = time.time()

		t_o = t2 - t1
		orientation_time.append(t_o)

		if K != None:
			
			if nx.is_strongly_connected(K):
			
				if n <= 6:
					t1 = time.time()
					d = nx.diameter(K)
					t2 = time.time()
	
				else:
					t1 = time.time()
					d = eulerian.approximate_diameter(K, sample_vertex_size)
					t2 = time.time()
	
				t_d = t2 - t1
				diameter_time.append(t_d)
				diameters.append(d)

		else:
			raise ValueError('maximum_matching_orientation is defined only for even n')

else:
	
	for i in range (sample_size):
		t1 = time.time()
		G = star_graph.oriented_n_star(n)
		t2 = time.time()

		t_c = t2 - t1
		orientation_time.append(t_c)

		if nx.is_strongly_connected(G):

			if n <= 6:
				t1 = time.time()
				d = nx.diameter(G)
				t2 = time.time()

			else:
				t1 = time.time()
				d = eulerian.approximate_diameter(G, sample_vertex_size)
				t2 = time.time()

			t_d = t2 - t1
			diameter_time.append(t_d)
			diameters.append(d)

if len(diameters) == 0:
	minimum_diameter = float('inf')
else:	
	minimum_diameter = min(diameters)

average_orientation_time = sum(orientation_time) / len(orientation_time)

if len(diameter_time) == 0:
	average_diameter_time = None
else:
	average_diameter_time = sum(diameter_time) / len(diameter_time)

if orientation == None:
	print('Construction time is', average_orientation_time)
else:
	print('Orientation time is', average_orientation_time)

print('Diameter calculation time is', average_diameter_time)
print('Diameter =', minimum_diameter)