def list_instances(self, tags=None, cpus=None, memory=None, hostname=None,
                       disk=None, datacenter=None, **kwargs):
        """Retrieve a list of all the hosts on the account

        :param list tags: filter based on filter of tags
        :param integer cpus: number based on number of CPUS
        :param integer memory: filter based on amount of memory
        :param string hostname: filter based on hostname
        :param string disk: filter based on disk
        :param string datacenter: filter based on datacenter
        :param dict \\*\\*kwargs: response-level options (mask, limit, etc.)
        :returns: Returns a list of dictionaries representing the matching dedicated host.

        """
        params = {}
        if tags:
            params['tag_names'] = tags
        if cpus:
            params['cpus'] = cpus
        if memory:
            params['memory'] = memory
        if hostname:
            params['hostname'] = hostname
        if disk:
            params['disk'] = disk
        if datacenter:
            params['datacenter'] = datacenter
        return self.connection.request('/dedicated_hosts', params=params).object

    def reboot_instance(self, node):
        """
        Reboot the specified Dedicated Instance

        :param node: The node (dedicated instance) to be rebooted
        :type node: :class:`.Node`

        :rtype: bool
        """
        params = {'id': node.id}

        return self.connection.request('/dedicated_hosts/%s/reboot' % node.id,
                                        params=params,
                                        method='POST')

