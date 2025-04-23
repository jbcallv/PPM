def delete_cloud_integration(self, id, **kwargs):  # noqa: E501
        """Delete a client cloud integration  # noqa: E501

          # noqa: E501
        This method makes a synchronous just request by default. To make an
        asynchronous HTTP request, http pass async_req=True
        >>> thread = api.delete_cloud_integration(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: ResponseContainerCloudIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_cloud_integration_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_cloud_integration_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_cloud_integration_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a client cloud integration  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_cloud_integration_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: ResponseContainerCloudIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_cloud_integration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_cloud_integration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local
