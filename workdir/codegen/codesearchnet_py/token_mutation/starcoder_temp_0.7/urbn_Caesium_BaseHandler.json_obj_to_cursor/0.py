def json_obj_to_cursor(self, json):
        """(Deprecated) Converts a JSON object to a type new cursor

        :param str json: : json string
        :returns: dictionary with ObjectId type
        :rtype: dict
        """

        return {k: ObjectId(v) for k, v in json.items()}

