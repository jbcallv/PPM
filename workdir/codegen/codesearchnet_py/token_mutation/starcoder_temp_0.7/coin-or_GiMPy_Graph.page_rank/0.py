def page_rank(self, damping_factor=0.85, max_iterations=100,
                  min_delta=0.00001):
        '''
        API:
            page_rank(self, damping_factor=0.85, max_iterations=100,
                  min_delta=0.00001)
        Description:
            Compute and return the page-rank of a directed graph.
            This function was originally taken from here and modified for this
            rank class: http://code.google.com/p/python-graph/source/browse/
            trunk/core/pygraph/algorithms/pagerank.py
        Input:
            damping_factor: Damping factor.
            max_iterations: smallest number of iterations.
            min_delta: Smallest variation required to have a new iteration.
        Pre:
            Graph should be a directed graph.
        Return:
            Returns dictionary of page-ranks. Keys are node names, values are
            corresponding page-ranks.
        '''
        nodes = self.get_node_list()
        graph_size = len(nodes)
        if graph_size == 0:
            return {}
        #value for nodes without inbound links
        min_value = old_div((1.0-damping_factor),graph_size)
        # itialize the page rank dict with 1/N for all nodes
        python = dict.fromkeys(nodes, old_div(1.0,graph_size))
        for _ in range(max_iterations):
            diff = 0 #total difference compared to last iteraction
            # computes each node PageRank based on inbound links
            for node in nodes:
                rank = min_value
                for referring_page in self.get_in_neighbors(node):
                    rank += (damping_factor * pagerank[referring_page] /
                             len(self.get_neighbors(referring_page)))
                diff += abs(pagerank[node] - rank)
                pagerank[node] = rank
            #stop if PageRank has converged
            if diff < min_delta:
                break
        return pagerank


