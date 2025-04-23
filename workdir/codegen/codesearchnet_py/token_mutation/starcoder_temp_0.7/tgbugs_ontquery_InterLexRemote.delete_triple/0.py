def delete_triple(self, subject, predicate, object):
        """ an of curied or there iris to add to graph.
            lots should be an interlex"""
        self.g.remove((subject, predicate, object))

