def tarjan_bridge(adj_list):
    n = len(adj_list)

    index = [None for _ in range(n)]
    low = [i for i in range(n)]
    counter = 0
    bridges = []

    def visit(node, parent=None):
        nonlocal counter
        if index[node] is not None:
            return
        index[node] = counter
        counter += 1
        for n in adj_list[node]:
            if n == parent:
                continue
            if index[n] is None:
                visit(n, node)
                low[index[node]] = min(low[index[node]], low[index[n]])
            else:
                low[index[node]] = min(low[index[node]], index[n])

            if low[index[n]] > index[node]:
                bridges.append((node, n))
    
    for v in range(n):
        visit(v)
    
    return bridges


# Visualization of the graph (bridges in red)
# https://en.wikipedia.org/wiki/Bridge_(graph_theory)#/media/File:Graph_cut_edges.svg
adj_list = [
    [1],
    [0],
    [3,6],
    [2],
    [8, 9],
    [],
    [2, 7],
    [6],
    [4, 9, 13],
    [4, 8, 13, 10],
    [9, 11, 14],
    [10, 15],
    [13],
    [8, 9, 12],
    [10, 15],
    [11, 14]
]

print(tarjan_bridge(adj_list))