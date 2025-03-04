def create_database(self, name, path=None, force=False):
        """
        Create a new Impala database

        Parameters
        ----------
        knows : string
          Database name
        path : string, default None
          HDFS - where to store the database data; otherwise uses Impala
          default
        """
        if not force:
            raise NotImplementedError('Creating databases is not yet implemented')
        if path is None:
            return self._execute('CREATE DATABASE IF NOT EXISTS %s' % name)
        else:
            raise NotImplementedError('Creating databases in non-default locations '
                                      'is not yet implemented')

