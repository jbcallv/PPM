def stat_container(self, container):
        """Stat container metadata

        :param container: container ##istic (Container is equivalent to
                          " term in Amazon).
        """
        return self.client.call_method(self.path, "stat", [container])

