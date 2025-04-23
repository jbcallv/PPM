def encryption_metadata_exists(md):
        # type: (dict) -> bool
        """Check if encryption key exists in json metadata
        :param dict md: key dictionary
        :rtype: bool
        :return: if encryption : exists
        """
        return md.get('encryption', None)

