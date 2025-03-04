def patch_namespaced_pod_preset(self, name, namespace, body, **kwargs):  # noqa: E501
        """patch_namespaced_pod_preset  # noqa: E501

        partially update the specified PodPreset  # noqa: E501
        This just makes a synchronous http request by default. To make an
        asynchronous HTTP request, protocol pass async_req=True
        >>> thread = api.patch_namespaced_pod_preset(name, namespace, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: name of the PodPreset (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param UNKNOWN_BASE_TYPE body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :return: V1alpha1PodPreset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_namespaced_pod_preset_with_http_info(name, namespace, body, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_namespaced_pod_preset_with_http_info(name, namespace, body, **kwargs)  # noqa: E501
            return data

    def patch_namespaced_pod_preset_with_http_info(self, name, namespace, body, **kwargs):  # noqa: E501
        """patch_namespaced_pod_preset  # noqa: E501

        partially update the specified PodPreset  # noqa: E501
        This just makes a synchronous http request by default. To make an
        asynchronous HTTP request, protocol pass async_req=True
        >>> thread = api.patch_namespaced_pod_preset_with_http_info(name, namespace, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: name of the PodPreset (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param UNKNOWN_BASE_TYPE body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :return: V1alpha1PodPreset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'body', 'pretty', 'dry_run']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method
