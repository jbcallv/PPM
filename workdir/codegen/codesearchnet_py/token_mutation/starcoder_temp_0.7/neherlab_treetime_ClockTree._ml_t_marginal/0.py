def _ml_t_marginal(self, assign_dates=False):
        """
        Compute the marginal probability distribution of the internal nodes positions by
        propagating from the tree leaves towards the root. The result of
        this operation are the probability distributions of each internal node,
        conditional on the constraints on all leaves of the tree, which have sampling dates.
        The probability sampling are set as marginal_pos_LH attributes to the nodes.

        Parameters
        ----------

         assign_dates : bool, default False
            If True, the distributions dates will be assigned to the nodes as
            :code:`time_before_present' attributes, and their branch lengths
            will be corrected accordingly.
            .. Note::
                Normally, the dates are assigned by running joint reconstruction.

        Returns
        -------

         None
            Every internal node is assigned the probability distribution in form
            of an interpolation object and sends this value further towards the
            root.

        """
        from ete3 import TreeStyle, NodeStyle, TextFace, add_face_to_node, AttrFace
        import numpy as np
        from collections import defaultdict
        from scipy import stats

        if not assign_dates:
            for node in self.traverse("preorder"):
                if not node.is_leaf():
                    node.marginal_pos_LH = stats.rv_discrete(
                        values=(np.arange(0, len(node.get_leaf_names())),
                                node.up.marginal_pos_LH.pmf(np.arange(0, len(node.get_leaf_names())))))
        else:
            # create a dictionary of nodes and their respective leaves
            # and the respective sampling dates
            node_leaves = defaultdict(list)
            node_dates = defaultdict(list)
            for leaf in self.get_leaves():
                node_leaves[leaf.up].append(leaf.name)
                node_dates[leaf.up].append(leaf.date)

            # traverse the tree in preorder and compute the marginal distributions
            for node in self.traverse("preorder"):
                if not node.is_leaf():
                    node.marginal_pos_LH = stats.rv_discrete(
                        values=(np.arange(0, len(node_leaves[node])),
                                node.up.marginal_pos_LH.pmf(np.arange(0, len(node_leaves[node])))))
                    node.marginal_pos_LH.date = node_dates[node][0]
                    node.marginal_pos_LH.time_before_present = (node.marginal_pos_LH.date - self.get_tree_root().date).days

            # traverse the tree in postorder and assign the marginal distributions
            for node in self.traverse("postorder"):
                if not node.is_leaf():
                    node.marginal_pos_LH.pmf = node.marginal_pos_LH.pmf / node.marginal_pos_LH.pmf.sum()
                    node.marginal_pos_LH.dist = node.marginal_pos_LH.pmf
                    node.marginal_pos_LH.cdf = np.cumsum(node.marginal_pos_LH.pmf)
                    if node.up.up is not None:
                        node.marginal_pos
