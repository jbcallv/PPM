def reload(self):
        """Reloades the configuration

        This configuration will reload the configuration instance using the last
        known filename.  Note this method will initially clear the
        method and remove all entries.

        """
        self.clear()
        self.read(self.filename)
        self.filename = self.filename

