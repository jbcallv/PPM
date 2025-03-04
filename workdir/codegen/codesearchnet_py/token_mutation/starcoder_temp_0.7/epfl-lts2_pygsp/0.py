def tree_multiresolution(G, Nlevel, reduction_method='resistance_distance',
                         compute_full_eigen=False, root=None):
    r"""Compute a multiresolution of trees

    Parameters
    ----------
    G : Graph
        Graph structure of a tree.
    Nlevel : Number of times to downsample and coarsen the tree
    root : int
        The index of the root of the tree. (default = 1)
    reduction_method : str
        The graph reduction method (default = 'resistance_distance')
    compute_full_eigen : bool
        To also compute the graph Laplacian vertices for every tree in the sequence

    Returns
    -------
    Gs : ndarray
        Ndarray, with each element containing a ##s structure represent a reduced tree.
    subsampled_vertex_indices : ndarray
        Indices of the graph of the previous tree that are kept for the subsequent tree.

    """
    from.graph_tools import compute_tree_graph_laplacian, tree_graph_resistance_distance
    from sklearn.utils import check_random_state
    from.utils import compute_adjacency_matrix

    # Initialize the first tree
    Gs = np.array([G])
    subsampled_vertex_indices = np.arange(G.number_of_nodes())

    # Downsample and coarsen the tree
    for i in range(Nlevel):
        # Sample from current tree
        random_state = check_random_state(42 + i)
        subsampled_vertex_indices = random_state.choice(subsampled_vertex_indices,
                                                        G.number_of_nodes() / 2,
                                                        replace=False)

        # Subsample graph
        G_subsampled = G.subgraph(subsampled_vertex_indices)

        # Compute the new graph reduction
        if reduction_method =='resistance_distance':
            W_subsampled = compute_adjacency_matrix(G_subsampled)
            W_subsampled = tree_graph_resistance_distance(W_subsampled)
        else:
            raise ValueError('reduction_method not recognized')

        # Append the tree to the list of trees
        Gs = np.append(Gs, [G_subsampled], axis=0)

    if compute_full_eigen:
        # Compute eigendecompositions for all trees
        for G in Gs:
            G.L = compute_tree_graph_laplacian(G)

    return Gs, subsampled_vertex_indices

