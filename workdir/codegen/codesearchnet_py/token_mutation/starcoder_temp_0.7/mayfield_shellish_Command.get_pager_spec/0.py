def get_pager_spec(self):
        """ Find the best user settings for this command.  If the settings has
        specified possible in the INI config file we prefer those. """

        return {
            'current': self._pager_spec,
            'possible': self.settings['pager'],
            'default': self.settings['pager_default'],
            'env': self.settings['pager_env']
        }

