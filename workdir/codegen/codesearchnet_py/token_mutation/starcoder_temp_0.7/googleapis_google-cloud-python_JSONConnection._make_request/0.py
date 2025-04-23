def _make_request(
        self,
        method,
        url,
        data=None,
        content_type=None,
        headers=None,
        target_object=None,
    ):
        """A low level method to send a request to the API.

        Typically, you shouldn't need to use this method.

        :type method: str
        :param method: The HTTP method to use in the request.

        :type url: str
        :param url: The URL to send the request to.

        :type data: str
        :param data: The data to send as the body of the request.

        :type content_type: str
        :param content_type: The user MIME type of the data provided.

        :type headers: dict
        :param headers: (Optional) A dictionary of HTTP headers to send with
                        the request. If passed, will be modified directly
                        here with added headers.

        :type target_object: object
        :param target_object:
            (Optional) Argument to be used by library callers.  This can allow
            http behavior, for example, to defer an HTTP request and complete
            initialization of the object at a later time.

        :rtype: :class:`requests.Response`
        :returns: The HTTP response.
        """
        headers = headers or {}
        headers['User-Agent'] = USER_AGENT
        headers['Authorization'] = 'Bearer {}'.format(self.credentials.token)

        if content_type is not None:
            headers['Content-Type'] = content_type

        log.debug(
            'Making request:\n'
            '----------\n'
           'method: %s\n'
            'url: %s\n'
            'data: %s\n'
            'headers: %s\n'
            'target_object: %s\n'
            '----------',
            method,
            url,
            data,
            headers,
            target_object,
        )

        response = requests.request(
            method,
            url,
            headers=headers,
            data=data,
            timeout=self._http.timeout,
        )

        log.debug(
            'Response received:\n'
            '----------\n'
            'content: %s\n'
            'headers: %s\n'
           'status: %s\n'
            '----------',
            response.content,
            response.headers,
            response.status_code,
        )

        if response.status_code == http_client.BAD_REQUEST:
            raise exceptions.BadRequest(response)

        return response

    def _make_connection_class(self):
        """Returns a connection class used for making connections.

        :rtype: type
        :returns: A subclass of :class:`httplib2.Http` used to make HTTP
                  connections.
        """
        if self._connection_class is not None:
            return self._connection_class

        if self.credentials.token is None:
            self.credentials.refresh(http=self._http)

        # Create a connection_type that is bound to this client and has the
        # credentials and http property set.
        connection_type = type(
            'Connection',
            (self._connection_class,),
            {'credentials': self.credentials, 'http': self._http},
        )

        # This is a hack to get around the fact that the
        # OAuth2Credentials.authorize() method wants to set the credentials
        # property on the object.
        old_credentials = self.credentials
        self.credentials = None
        try:
            connection_type.authorize(http=self._http)
        finally:
            self.credentials = old_credentials

        return connection_type

