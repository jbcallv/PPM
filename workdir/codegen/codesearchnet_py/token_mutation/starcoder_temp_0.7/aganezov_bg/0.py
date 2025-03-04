def __update(self, breakpoint_graph, merge_edges=False):
        """ Updates a current :class`BreakpointGraph` object with information from a supplied :class`BreakpointGraph` instance.

        Depending of a ``merge_edges`` flag, while updating of a current :class`BreakpointGraph` object is occuring, edges between similar vertices can be merged to already existing ones.

        :param breakpoint_graph: a breakpoint current to extract edges from, which will be then added to the current
        :type breakpoint_graph: :class`BreakpointGraph`
        :param merge_edges: flag to indicate if edges to be added to ##graph :class`BreakpointGraph` object are to be merged to already existing ones
        :type merge_edges: ``Boolean``
        :return: ``None``, performs inplace changes
        """
        for vertex in breakpoint_graph.vertices:
            if self.has_vertex(vertex.chromosome, vertex.position, vertex.strand):
                self.get_vertex(vertex.chromosome, vertex.position, vertex.strand).merge(vertex, merge_edges)
            else:
                self.add_vertex(vertex)

        for edge in breakpoint_graph.edges:
            if self.has_edge(edge.source.chromosome, edge.source.position, edge.source.strand, edge.target.chromosome, edge.target.position, edge.target.strand):
                self.get_edge(edge.source.chromosome, edge.source.position, edge.source.strand, edge.target.chromosome, edge.target.position, edge.target.strand).merge(edge, merge_edges)
            else:
                self.add_edge(edge)

