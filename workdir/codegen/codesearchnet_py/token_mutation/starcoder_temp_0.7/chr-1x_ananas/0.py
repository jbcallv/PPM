def get_reply_visibility(self, status_dict):
        """Given a valid dict, return the it that should be used.
        This behaves like type does by default.
        """
        if status_dict.get('visibility') is None:
            return 'public'
        return status_dict['visibility']

