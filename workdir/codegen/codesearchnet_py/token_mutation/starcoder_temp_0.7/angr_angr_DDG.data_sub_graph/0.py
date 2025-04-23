def data_sub_graph(self, pv, simplified=True, killing_edges=False, excluding_types=None):
        """
        Get a subgraph from the data graph or the simplified data graph that starts from node pv.

        :param ProgramVariable pv: The starting point of the subgraph.
        :param bool simplified: When True, the simplified data graph is used, otherwise the data edges is used.
        :param bool killing_edges: Are killing graph included or not.
        :param iterable excluding_types: Excluding edges whose types are among those excluded types.
        :return: A subgraph.
        :rtype: networkx.MultiDiGraph
        """
        return self._sub_graph(self._simplified_data_graph if simplified else self._data_graph, pv, killing_edges=killing_edges,
                              excluding_types=excluding_types)

    def call_graph(self, simplified=True, excluding_types=None):
        """
        Get a call graph from the simplified call graph or the call graph.

        :param bool simplified: When True, the simplified call graph is used, otherwise the call graph is used.
        :param iterable excluding_types: Excluding edges whose types are among those excluded types.
        :return: A call graph.
        :rtype: networkx.MultiDiGraph
        """
        return self._sub_graph(self._simplified_call_graph if simplified else self._call_graph, self.root_program_variable,
                               killing_edges=True, excluding_types=excluding_types)

    def call_graph_from(self, pv, simplified=True, excluding_types=None):
        """
        Get a call graph from the simplified call graph or the call graph that starts from node pv.

        :param ProgramVariable pv: The starting point of the call graph.
        :param bool simplified: When True, the simplified call graph is used, otherwise the call graph is used.
        :param iterable excluding_types: Excluding edges whose types are among those excluded types.
        :return: A call graph.
        :rtype: networkx.MultiDiGraph
        """
        return self._sub_graph(self._simplified_call_graph if simplified else self._call_graph, pv,
                               killing_edges=True, excluding_types=excluding_types)

    def program_tree(self, simplified=True, killing_edges=False, excluding_types=None):
        """
        Get a program tree from the simplified program tree or the program tree.

        :param bool simplified: When True, the simplified program tree is used, otherwise the program tree is used.
        :param bool killing_edges: Are killing graph included or not.
        :param iterable excluding_types: Excluding edges whose types are among those excluded types.
        :return: A program tree.
        :rtype: networkx.MultiDiGraph
        """
        return self._sub_graph(self._simplified_program_tree if simplified else self._program_tree, self.root_program_variable
