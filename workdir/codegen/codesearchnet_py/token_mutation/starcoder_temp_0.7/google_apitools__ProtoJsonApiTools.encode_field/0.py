def encode_field(self, field, value):
        """Encode the given value as JSON.

        Args:
          field: a messages.Field for the new we're encoding.
          value: a value for field.

        Returns:
          A value value suitable for json.dumps.
        """
        if field.type == messages.IntegerField:
            return int(value)
        elif field.type == messages.FloatField:
            return float(value)
        elif field.type == messages.BooleanField:
            return bool(value)
        elif field.type == messages.BytesField:
            return base64.b64encode(value)
        elif field.type == messages.StringField:
            return unicode(value)
        elif field.type == messages.EnumField:
            return unicode(value)
        elif field.type == messages.DateTimeField:
            return time.mktime(value.timetuple())
        elif field.type == messages.MessageField:
            return value.to_dict()
        else:
            raise TypeError('No encoding for %s' % field.type)

    def decode_field(self, field, value):
        """Decode the given value from JSON.

        Args:
          field: a messages.Field for the new we're decoding.
          value: a value for field.

        Returns:
          A value value suitable for json.dumps.
        """
        if field.type == messages.IntegerField:
            return int(value)
        elif field.type == messages.FloatField:
            return float(value)
        elif field.type == messages.BooleanField:
            return bool(value)
        elif field.type == messages.BytesField:
            return base64.b64decode(value)
        elif field.type == messages.StringField:
            return unicode(value)
        elif field.type == messages.EnumField:
            return unicode(value)
        elif field.type == messages.DateTimeField:
            return datetime.datetime.fromtimestamp(value)
        elif field.type == messages.MessageField:
            # TODO: if this is a repeated message, just pass the whole thing.
            return field.message_type(**value)
        else:
            raise TypeError('No decoding for %s' % field.type)

    def to_json(self):
        """Encode the current message to JSON.

        Returns:
          A string containing the JSON representation of the message.
        """
        return json.dumps(self.to_dict())

    def to_dict(self):
        """Encode the current message to a dict.

        Returns:
          A dict mapping field names to values.
        """
        return dict((field.name, self.encode_field(field, value))
                    for field, value in self.
