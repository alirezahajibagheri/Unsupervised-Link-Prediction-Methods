def common_neighbors_score(graph):
    
	n = graph.vcount()
    common_neis = np.zeros((n, n))
    for v in range(graph.vcount()):
        neis = graph.neighbors(v)
        for u, w in combinations(neis, 2):
            # v is a common neighbor of u and w
            common_neis[u, w] += 1
            common_neis[w, u] += 1
	
	return common_neis