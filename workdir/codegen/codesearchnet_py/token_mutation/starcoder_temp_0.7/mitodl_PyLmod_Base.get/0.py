def get(self, service, params=None):
        """Generic GET method for retrieving data from Learning Modules API.

        .. code-block:: python

            gbk.get('students/{gradebookId}', params=params, gradebookId=gbid)

        Args:
            service (str): The endpoint code to use, i.e. gradebook
            params (dict): additional parameters to add to the call

        Raises:
            requests.RequestException: Exception connection error
            ValueError: Unable to decode response content

        Returns:
            list: the json-encoded content of the response
        """
        return self._get(service, params=params)

