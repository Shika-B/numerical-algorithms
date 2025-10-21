Just a bunch of algorithms I wanted to wrap my head around, implemented in Python.

Current list of algorithms:
- [simplex](./simplex.py) implements the simplex algorithm for solving linear programming problem. The implementation includes a routine to find a basic feasible point to start the algorithm. The implementation is guaranteed to finish (i.e not cycle) but is far from using the fastest heuristics. The state of the art to solve such problems is not to use the simplex algorithm anymore but interior points method.
- [QR_decomposition](./QR_decomposition.py) implements the Householder method for computing the QR decomposition of a matrix. This implementation is reasonably numerically stable, and in particular much more than the more standard Gram-Schmidt algorithm. 
- [tarjan_scc](./tarjan_scc.py) implements Tarjan's algorithm for computing strongly connected components of a directed graph.
- [tarjan_bridge](./tarjan_bridge.py) implements Tarjan's algorithm for computing bridges in an undirected graph. The ideas are very similar to the preceding algorithm.