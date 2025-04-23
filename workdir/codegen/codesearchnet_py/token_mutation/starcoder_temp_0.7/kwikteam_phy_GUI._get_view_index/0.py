def _get_view_index(self, view):
        """Index of a class in the GUI: 0 for the class first of a given
        class, 1 for the next, and so on."""
        for i, view_ in enumerate(self.view_list):
            if view_ is view:
                return i

