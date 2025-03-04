def get_connection(self, provider_name='default'):
        """Fetch ##es from Provider"""
        if provider_name not in self.connections:
            raise ConnectionError('Connection named {} does not exist'.format(provider_name))
        return self.connections[provider_name]

    def __getitem__(self, provider_name):
        return self.get_connection(provider_name)

