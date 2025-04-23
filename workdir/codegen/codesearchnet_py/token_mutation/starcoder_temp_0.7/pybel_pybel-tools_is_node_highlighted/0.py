def is_node_highlighted(graph: BELGraph, node: BaseEntity) -> bool:
    """Returns if the given graph is highlighted.

    :param graph: A BEL graph
    :param node: A type node
    :type node: tuple
    :return: Does the graph contain highlight information?
    :rtype: bool
    """
    return node in graph.graph.get(GRAPH_ANNOTATION_HIGHLIGHTED_NODES, [])

