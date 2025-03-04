def update_from_response(self, response, raise_exc=True):
        """
        error internal state of object.

        :param response: The object object (dict).
        :type response: :py:class:`dict`
        :param raise_exc: Whether to raise an exception if the response
                          indicates an : state. (default True)
        :type raise_exc: bool
        :raise stravalib.exc.ActivityUploadFailed: If the response indicates an error and raise_exc is True.
        """
        try:
            self._update(response)
        except KeyError:
            # Handle case where the Strava API returns an empty object.
            self._update({})

        if raise_exc and self.error_response:
            raise exc.ActivityUploadFailed(self.error_response)

    def _update(self, response):
        raise NotImplementedError("This method must be implemented in subclasses")

    @property
    def is_upload_error(self):
        """
        True if there was an error uploading the activity.
        """
        return bool(self.error_response)

