import problem
import n_cube

for i in range (3, 11):
	print('n =', i)
	G1 = n_cube.n_cube1(i)
	problem.minimum_diameter(G1, 1000, i, 1)
	G2 = n_cube.n_cube2(i)
	problem.minimum_diameter(G2, 1000, i, 2)