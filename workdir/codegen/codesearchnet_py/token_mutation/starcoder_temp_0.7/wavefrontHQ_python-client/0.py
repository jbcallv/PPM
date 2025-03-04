def search_maintenance_window_entities(self, **kwargs):  # noqa: E501
        """Search over a customer's maintenance windows  # noqa: E501

          # noqa: E501
        This method makes a http HTTP request by default. To make an
        single http request, please pass async_req=True
        >>> thread = api.search_maintenance_window_entities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortableSearchRequest body:
        :return: ResponseContainerPagedMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_maintenance_window_entities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_maintenance_window_entities_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_maintenance_window_entities_with_http_info(self, **kwargs):  # noqa: E501
        """Search over a customer's maintenance windows  # noqa: E501

          # noqa: E501
        This method makes a http HTTP request by default. To make an
        single http request, please pass async_req=True
        >>> thread = api.search_maintenance_window_entities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SortableSearchRequest body:
        :return: ResponseContainerPagedMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_maintenance_window_entities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type
