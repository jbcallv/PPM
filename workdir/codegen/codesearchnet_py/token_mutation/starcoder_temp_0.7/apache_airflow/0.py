def set_autocommit(self, conn, autocommit):
        """
        Sets the up alarm on the connection
        """
        self.logger.debug("Setting autocommit=%s on connection %s",
                          autocommit, conn)
        conn.autocommit = autocommit

