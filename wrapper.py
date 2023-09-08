import problem
import n_cube

for i in range (3, 11):
	print('n =', i)
	n_cube.n_cube1(i)
	problem.minimum_diameter(f'matrix1_n{i}.txt', 1000, i, 1)
	n_cube.n_cube2(i)
	problem.minimum_diameter(f'matrix2_n{i}.txt', 1000, i, 2)