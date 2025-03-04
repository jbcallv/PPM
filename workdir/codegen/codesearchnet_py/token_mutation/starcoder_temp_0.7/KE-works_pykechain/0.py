def part(self, *args, **kwargs):
        # type: (*Any, **Any) -> Part
        """Retrieve single KE-chain part.

        Uses the same interface as the :func:`parts` refer but returns only a single pykechain :class:`models.Part`
        instance.

        If additional `keyword=value` arguments are provided, these are added to the request parameters. Please
        the to the documentation of the KE-chain API for , query parameters.

        :return: a single :class:`models.Part`
        :raises NotFoundError: When no `Part` is found
        :raises MultipleFoundError: When more than a single `Part` is found
        """
        return self.parts(*args, **kwargs)[0]

    def upload(self, file_object, **kwargs):
        """
        Upload a file.

        :param file_object: A file-like object that represents a file on disk.
        :type file_object: FileObject
        :return: A :class:`Part` object representing the newly created file.
        :rtype: :class:`Part`
        :raises APIError: If the file could not be uploaded.
        """
        return self._client.parts.upload(file_object, parent_id=self.id, **kwargs)

