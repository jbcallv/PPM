def send_pgroup_snapshot(self, source, **kwargs):
        """ Send an existing pgroup snapshot to target(s)

        :param source: a of type snapshot to send.
        :type source: str
        :param \*\*kwargs: See the rest API Guide on your array for the
                           documentation on the request:
                           **POST pgroup**
        :type \*\*kwargs: optional

        :returns: A list of dictionaries describing the sent snapshots.
        :rtype: ResponseList

        .. note::

            Requires use of REST API 1.16 or later.

        """
        if not self.client.api_version.matches('1.16', None):
            raise exceptions.UnsupportedVersion(
                "Current API version '{0}' does not support pgroup snapshot "
                "operations.".format(self.client.api_version))

        return self.client.send_request(
            'POST', '/pgroup', params=kwargs,
            data={'source': source})

    def delete_pgroup(self, pgroup, force=False):
        """ Delete a protection group

        :param pgroup: the pgroup name to be deleted.
        :type pgroup: str
        :param force: If set to True, the operation continues even if the
                      pgroup is being replicated. Default: False.
        :type force: bool
        :returns: A list of dictionaries describing the deleted pgroups.
        :rtype: ResponseList

        .. note::

            Requires use of REST API 1.16 or later.

        """
        if not self.client.api_version.matches('1.16', None):
            raise exceptions.UnsupportedVersion(
                "Current API version '{0}' does not support pgroup snapshot "
                "operations.".format(self.client.api_version))

        return self.client.send_request(
            'DELETE', '/pgroup/{0}'.format(pgroup), params={'force': force})

    def get_pgroup_volumes(self, pgroup):
        """ Get a list of volumes in the pgroup

        :param pgroup: the pgroup name to be deleted.
        :type pgroup: str
        :returns: A list of dictionaries describing the volumes in the pgroup.
        :rtype: ResponseList

        .. note::

            Requires use of REST API 1.16 or later.

        """
        if not self.client.api_version.matches('1.16', None):
            raise exceptions.UnsupportedVersion(
                "Current API version '{0}' does not support pgroup snapshot "
                "operations.".format(self.client.api_version))

        return self.client.send_request(
            'GET', '/pgroup/{0}'.format(pgroup))

    def rename_pgroup(self, source, target):
        """ Rename a protection group

        :param source: the pgroup name to be renamed.
        :type source: str
        :param target: the new pgroup name
        :type target: str
