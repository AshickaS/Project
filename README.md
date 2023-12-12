# Implementation of Graph Algorithms in NetworkX
**Aim:**  To choose a graph algorithm not already available in the opensource networkx library and implement the same with a view to integrate it with the library.

An **interconnected network** is a system where multiple individual networks are linked together to form a large, more complex network. In interconnected networks, **orientation** refers to the directionality of connections between nodes. We use **Cayley graphs** to model and analyze the structure of the network and its connections. We have to find the **minimum oriented diameter** of the Cayley graphs.  The two types of Cayley graphs we are interested in are $n\text{-cube}$ and $n\text{-star}$.
## $n\text{-cube}$
The files associated with the problem are:
* n_cube.py

  Contains two functions `n_cube1` and `n_cube2` that returns the graph $n\text{-cube}$ for an $n$ in two different approaches.

* functions.py

  Contains two functions `is_undirected` and `to_undirected`. The function `to_undirected` is used by n_cube.py

* problem.py

  Contains the function `minimum_diameter` that calculates the minimum oriented diameter of a graph $G$.

* wrapper.py

  Run this file to find the minimum oriented diameter. The output are text files with filename output_{n2}_{n1}. n2 is 1 or 2 according as the use of the functions `n_cube1` or `n_cube2`. n1 denotes the $n$ in $n\text{-cube}$.
## $n\text{-star}$
The files associated with the problem are:
* star_graph.py

  Contains two functions `n_star` and `oriented_n_star`. The function `n_star` returns an $n\text{-star}$ for an $n$. The fuction `oriented_n_star` recursively generates an oriented $n\text{-star}$ for an $n$.

* relabel.py

  Contains two functions `relabel` and `bulk_relabel`. The `bulk_relabel` function is used by the `oriented_n_star`.

* eularian.py

  * The following three functions orient a graph $G$ using different approaches.
      * `random_walk_orientation`
      * `eulerian_orientation_with_cycles`
      * `maximum_matching_orientation`
  * The function `approximate_diameter` is used by wrapper_n_star.py for large values of $n$.

* wrapper_n_star.py

  Run this file to find the minimum oriented diameter of $n\text{-star}$. Set the parameters n, sample_size, orientation and sample_vertex_size.
  
