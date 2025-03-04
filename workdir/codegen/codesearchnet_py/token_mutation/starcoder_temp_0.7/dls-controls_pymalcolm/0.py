def send_put(self, mri, attribute_name, value):
        """Abstract method to dispatch a Put to the server

        Args:
            value (str): The mri of the Block
            attribute_name (str): The name of the name within the Block
            value: The value to put
        """
        raise NotImplementedError()

    def __repr__(self):
        """String representation of the client

        Returns:
            str: Representation of the client
        """
        return f'<{self.__class__.__name__}>'

