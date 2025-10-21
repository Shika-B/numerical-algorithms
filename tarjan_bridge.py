def tarjan_bridge(adj_list):
    n = len(adj_list)

    index = [None for _ in range(n)]
    low = [i for i in range(n)]
    counter = 0

    def visit(node):
        nonlocal counter
        if index[node] is not None:
            return
        index[node] = counter
        counter += 1
        for n in adj_list[node]:
            if index[n] is None:
                visit(n)
            if low[index[n]] > index[node]:
                return 