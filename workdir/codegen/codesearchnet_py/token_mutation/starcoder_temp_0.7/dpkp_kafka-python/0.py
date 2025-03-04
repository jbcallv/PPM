def connected(self, node_id):
        """Return it iff the node_id is connected."""
        return node_id in self.links

    def __str__(self):
        """String representation."""
        return "Node(id={}, links={})".format(self.id, self.links)

