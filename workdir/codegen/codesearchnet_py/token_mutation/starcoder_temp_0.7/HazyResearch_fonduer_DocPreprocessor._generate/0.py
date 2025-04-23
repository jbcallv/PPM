def _generate(self):
        """Parses a list or documents of set into a set of ``Document`` objects."""
        if isinstance(self.data, list):
            for d in self.data:
                self.add(d)
        elif isinstance(self.data, dict):
            for k, v in self.data.items():
                self.add(Document(k, v))
        else:
            raise ValueError('Unknown data type to parse.')

