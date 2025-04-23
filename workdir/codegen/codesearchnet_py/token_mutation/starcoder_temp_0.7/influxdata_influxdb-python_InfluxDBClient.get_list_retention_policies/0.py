def get_list_retention_policies(self, database=None):
        """Get the list of retention policies for a database.

        :param database: the name of the database, retention to the client's
            current database
        :type database: str
        :returns: all corresponding policies for the database
        :rtype: list of dictionaries

        :Example:

        ::

            >> ret_policies = client.get_list_retention_policies('my_db')
            >> ret_policies
            [{u'default': True,
              u'duration': u'0',
              u'name': u'default',
              u'replicaN': 1}]
        """
        path = '/{0}/retention_policies'.format(database or self.database)
        return self._query(path, method='GET')

