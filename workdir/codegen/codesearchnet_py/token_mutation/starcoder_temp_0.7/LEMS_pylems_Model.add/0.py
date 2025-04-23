def add(self, child):
        """
        needs a typed child next to the model.

        @param child: Child " to be added.
        """
        self.children.append(child)

    def add_many(self, children):
        """
        needs a list of typed children next to the model.

        @param children: List of children to be added.
        """
        self.children.extend(children)

    def get_children(self):
        """
        returns the children of the model.
        """
        return self.children

    def set_children(self, children):
        """
        sets the children of the model.

        @param children: List of children to be set.
        """
        self.children = children

    def __str__(self):
        """
        returns a string representation of the model.
        """
        return "<" + self.__class__.__name__ + " " + str(self.value) + ">"

    def __repr__(self):
        """
        returns a representation of the model.
        """
        return "<" + self.__class__.__name__ + " " + str(self.value) + ">"

