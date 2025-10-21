"""
Implements the following algorithm https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""

def tarjan_scc(adj_list):
    """
    Assumes the graph is given as an adjacency list
    """
    n = len(adj_list)
    counter = 0
    index = [None for _ in range(n)]
    low = [i for i in range(n)]
    counter = 0
    stack = []
    scc_list = []
    def visit(node):
        nonlocal counter
        if index[node] is not None:
            return
        stack.append(node)
        index[node] = counter
        counter += 1
        for n in adj_list[node]:
            if index[n] is None:
                visit(n)
                low[node] = min(low[node], low[n])
            else:
                low[node] = min(low[node], index[n])
        if low[node] == index[node]:
            scc = []
            while stack and stack[-1] != node:
                scc.append(stack.pop())
            scc.append(stack.pop())
            scc_list.append(scc)
    for v in range(n):
        visit(v)        
    return scc_list

# See here for a visual of the test graph:
# https://en.wikipedia.org/wiki/Strongly_connected_component#/media/File:Scc-1.svg

adj_list = [
    [1],
    [2, 4, 5],
    [6, 3],
    [2, 7],
    [0, 5],
    [6],
    [5],
    [3, 6]
]

print(tarjan_scc(adj_list))