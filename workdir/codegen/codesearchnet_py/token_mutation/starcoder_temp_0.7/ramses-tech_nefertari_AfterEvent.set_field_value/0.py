def set_field_value(self, field_name, value):
        """ Set value of response field named `field_name`.

        If response contains single item, its items is set.
        If response contains multiple items, all the value in response
        are edited.
        To edit response meta(e.g. 'count') edit response directly at
        `event.response`.

        :param field_name: Name of the field value of which should
            be set.
        :param value: Value to be set.
        """
        if not isinstance(self.response, list):
            self.response = [self.response]

        for item in self.response:
            setattr(item, field_name, value)

