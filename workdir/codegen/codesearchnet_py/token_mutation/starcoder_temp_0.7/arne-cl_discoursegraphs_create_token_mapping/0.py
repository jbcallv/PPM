def create_token_mapping(docgraph_with_old_names, docgraph_with_new_names,
                         verbose=False):
    """
    given two document graphs which annotate the same text and which use the
    same tokenization, creates a dictionary with a mapping from the token
    IDs used in the first graph to the token IDs used in the second graph.

    Parameters
    ----------
    docgraph_with_old_names : DiscourseDocumentGraph
        a document graph with token IDs that will be replaced later on
    docgraph_with_new_names : DiscourseDocumentGraph
        a document graph with token IDs that will replace the token IDs
        used in ``docgraph_with_old_names`` later on

    Returns
    -------
    old2new : dict
        maps from a token ID used in ``docgraph_with_old_names`` to the token
        ID used in ``docgraph_with_new_names`` to reference the same token
    """
    old2new = {}
    for old_token_id, new_token_id in zip(
            docgraph_with_old_names.get_tokens(),
            docgraph_with_new_names.get_tokens()):
        old2new[old_token_id] = new_token_id
    return old2new

