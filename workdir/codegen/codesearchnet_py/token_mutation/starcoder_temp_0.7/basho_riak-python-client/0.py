def get_resources(self):
        """
        Gets a list domain of server-side full names to paths
        :rtype dict
        """
        return self.resources

    def get_resource_path(self, resource):
        """
        Get the absolute path of a resource from a name
        :param resource: server-side full name of the resource
        :rtype string
        """
        return self.resources.get(resource, '')

