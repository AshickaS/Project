# Implementation of Graph Algorithms in NetworkX

## Interconnected Networks and Cayley Graphs
An **interconnected network** is a system where multiple individual networks are linked together to form a large, more complex network. These networks play a crucial role in various domains, including computer systems, communication networks, and parallel computing. In interconnected networks, **orientation** refers to the directionality of connections between nodes. This factor is pivotal in influencing the flow and efficiency of information or resource exchange across multiple networks. We use **Cayley graphs** to model and analyze the structure of the network and its connections. 

Suppose we have a group $<\mathcal{G}, \*>$ with generating set $S$. For any $g\in \mathcal{G}$ and $s \in S$ there exists an edge from $g$ to $g*s$. Such a graph is called a Cayley graph. The particular Cayley graph with which we are working is a **Star graph**.  An $n$-star is a graph denoted by $S_n$ which has $n!$ vertices, each of which represents a permutation of $n$ symbols (we have used the letters $a,b,c ,\ldots$ for labels) and has edges between those vertices whose labels differ only in the first and any one more position. Our interest is to find the **minimum oriented diameter**, that is the shortest diamter among all orientations of the $n\text{-star}$.

The **aim** of this project is to try to find an orientation with a smaller diameter, further improving the best known bound of $2n+4$ to a value closer to $1.5n$.
## Orientations of the $n\text{-star}$
 Various orientations tried include:

 Algorithm 1. **Maximum distance pair path orientation:**
 > This orientation serves as a benchmark and further improvements are made.

 Algorithm 2. **Random walk model:**
 > This method orients the graph using a random walk. This method is completely
 random.

 Algorithm 3. **Random walk with unvisited vertex preference:**
 >This method is a modification of the previous method in which we prefer the unvisited
 vertices over the visited vertices on the walk.

 Algorithm 4. **Eulerian orientation:**
 >This method was introduced in view of reducing the indgree-outdgree difference
 caused by the previous method.

 Algorithm 5. **All pairs prior maximum distance cycle orientation:**
 >This method is a modification of the last one in which we prefer larger cycles to be
 oriented first.

 Algorithm 6. **All pairs maximum distance cycle orientation:**
 >This method is a further modification in which the current larger cycles in each
 updation are oriented.
 
 Algorithm 7. **Maximum distance pair cycle orientation:**
 >We modify the algorithm further to make it faster by calculating the maximum more
 efficiently.
 
 Algorithm 8. **Random vertex pair maximum distance orientation:**
 >This method is introduced in view of further increasing the computational speed.
 
 Algorithm 9. **Recursive orientation:**
 >This method uses a completely different approach from the previous methods. In this
 method, we recursively generate an oriented graph

The files associated with the problem are:
* [star_graph.py](https://github.com/AshickaS/Project/blob/main/star_graph.py)

  Contains two functions [`n_star`](https://github.com/AshickaS/Project/blob/main/star_graph.py#L9) and [`oriented_n_star`](https://github.com/AshickaS/Project/blob/main/star_graph.py#L9). The function `n_star` returns an $n\text{-star}$ for an $n$. The fuction `oriented_n_star` recursively generates an oriented $n\text{-star}$ for an $n$.

* [relabel.py](https://github.com/AshickaS/Project/blob/main/relabel.py)

  Contains two functions [`relabel`](https://github.com/AshickaS/Project/blob/main/relabel.py#L1) and [`bulk_relabel`](https://github.com/AshickaS/Project/blob/main/relabel.py#L21). The `bulk_relabel` function is used by the `oriented_n_star`.

* [eularian.py](https://github.com/AshickaS/Project/blob/main/eulerian.py)

  * The following functions orient a graph $G$ using different approaches.
      * Algorithm 1: [`maximum_distance_pair_orientation`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L133)
      * Algorithm 2: [`random_walk_orientation`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L5)
      * Algorithm 3: [`random_walk_orientation_new`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L26)
      * Algorithm 4a: [`eulerian_orientation_with_cycles`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L53)
      * Algorithm 4b: [`maximum_matching_orientation`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L89)
      * Algorithm 5: [`initial_max_cycle_orientation`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L149)
      * Algorithm 6: [`all_pairs_max_cycle_orientation`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L171)
      * Algorithm 7: [`max_cycle_orientation`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L202)
      * Algorithm 8: [`random_pair_max_dist_orientation`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L238)
  * Additional functions used are:
      * [`max_dist_pair_path`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L277)
      * [`path`](https://github.com/AshickaS/Project/blob/main/eulerian.py#L296)

* [5_star.py](https://github.com/AshickaS/Project/blob/main/5_star.py)

  **Run this file** to find the minimum oriented diameter of $n\text{-star}$. Set the parameters `n`, `test_number`, uncomment the required `orientation`.
  
