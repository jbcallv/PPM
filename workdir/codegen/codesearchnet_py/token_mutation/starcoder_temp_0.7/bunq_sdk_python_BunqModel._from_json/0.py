def _from_json(cls, response_raw, wrapper=None):
        """
        :type response_raw: client.BunqResponseRaw
        :type wrapper: str|None

        :rtype: client.BunqResponse[cls]
        """

        return converter.json_to_class(cls, response_raw.body_bytes, wrapper)

