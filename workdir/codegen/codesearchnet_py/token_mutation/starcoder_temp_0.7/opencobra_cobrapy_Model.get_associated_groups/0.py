def get_associated_groups(self, element):
        """Returns a list of groups that an element (reaction, metabolite, gene)
        is associated with.

        Parameters
        ----------
        element: `cobra.Reaction`, `cobra.Metabolite`, or `cobra.Gene`

        Returns
        -------
        list of `cobra.Group`
            All groups that the object object is a member of
        """
        return list(set(element.groups.values()))

    def get_associated_group_members(self, group):
        """Returns a list of elements that are members of a group.

        Parameters
        ----------
        group: `cobra.Group`
            The group to get members of

        Returns
        -------
        list of `cobra.Reaction`, `cobra.Metabolite`, or `cobra.Gene`
            All objects that are members of the group
        """
        members = []
        for member in group.members:
            members.append(member)
        return members

    def get_associated_group_names(self, element):
        """Returns a list of names of groups that an element (reaction, metabolite, gene)
        is associated with.

        Parameters
        ----------
        element: `cobra.Reaction`, `cobra.Metabolite`, or `cobra.Gene`

        Returns
        -------
        list of `cobra.Group`
            All groups that the object object is a member of
        """
        return [group.id for group in self.get_associated_groups(element)]

    def get_associated_group_names_of_metabolite(self, metabolite):
        """Returns a list of names of groups that a metabolite is associated with.

        Parameters
        ----------
        metabolite: `cobra.Metabolite`
            The metabolite to get group names of

        Returns
        -------
        list of `cobra.Group`
            All groups that the metabolite is a member of
        """
        return [group.id for group in self.get_associated_groups(metabolite)]

