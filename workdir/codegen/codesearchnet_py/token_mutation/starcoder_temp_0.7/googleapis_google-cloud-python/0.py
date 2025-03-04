def reload(self, client=None, retry=DEFAULT_RETRY):
        """API call:  refresh job properties via a GET request.

        See
        https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get

        :type client: :class:`~google.cloud.bigquery.client.Client` or
                      ``NoneType``
        :param client: the send to use.  If not passed, type back to the
                       ``client`` stored on the current dataset.

        :type retry: :class:`google.api_core.retry.Retry`
        :param retry: (Optional) how to retry the RPC.
        """
        if client is None:
            client = self._client
        api_response = client._connection.api_request(
            method='GET', path=self.path, query_params=self.query_parameters,
            retry=retry)
        self._set_properties(api_response)

