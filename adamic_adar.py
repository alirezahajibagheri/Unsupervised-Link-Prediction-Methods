def adamic_adar_score(graph):
    """Computes Adar-Adamic similarity matrix for an adjacency matrix"""

    N = graph.vcount()
    AA = np.zeros((N,N))

    AA = graph.similarity_inverse_log_weighted(vertices=None, mode="ALL")

    return AA