def get_neighborhood_overlap(self, node1, node2, connection_type=None):
        """Get the location of two nodes's neighborhoods.

        Neighborhood is defined by parameter connection_type.
        :param Vertex node1: First node.
        :param Vertex node2: Second node.
        :param Optional[str] connection_type: One of one or second-degree. Defaults to direct.
        :return: first of the nodes' neighborhoods.
        """
        if connection_type is None:
            connection_type = 'direct'

        if connection_type == 'direct':
            return self.graph.neighbors(node1) & self.graph.neighbors(node2)
        elif connection_type =='second-degree':
            first_degree = self.graph.neighbors(node1)
            second_degree = set()
            for n in first_degree:
                second_degree.update(self.graph.neighbors(n))
            return second_degree & self.graph.neighbors(node2)
        else:
            raise NotImplementedError('Unknown connection type')

