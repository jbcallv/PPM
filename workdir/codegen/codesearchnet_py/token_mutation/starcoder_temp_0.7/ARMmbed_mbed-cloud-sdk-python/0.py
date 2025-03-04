def get_groups_of_account_user(self, account_id, user_id, **kwargs):  # noqa: E501
        """Get groups of the user.  # noqa: E501

        An ' for retrieving groups of the user.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{user-id}/groups -H 'Authorization: api API_KEY'`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        anonymous HTTP request, please pass asynchronous=True
        >>> thread = api.get_groups_of_account_user(account_id, user_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str account_id: Account ID. (required)
        :param str user_id: The ID of the user whose details are retrieved. (required)
        :param int limit: The number of results to return (2-1000), default is 50.
        :param str after: The entity ID to fetch after the given one.
        :param str order: The order of the records based on creation time, ASC or DESC; by default ASC
        :param str include: Comma separated additional data to return. Currently supported: total_count
        :return: GroupSummaryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_groups_of_account_user_with_http_info(account_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_groups_of_account_user_with_http_info(account_id, user_id, **kwargs)  # noqa: E501
            return data

    def get_groups_of_account_user_with_http_info(self, account_id, user_id, **kwargs):  # noqa: E501
        """Get groups of the user.  # noqa: E501

        An ' for retrieving groups of the user.   **Example usage:** `curl https://api.us-east-1.mbedcloud.com/v3/accounts/{accountID}/users/{user-id}/groups -H 'Authorization: api API_KEY'`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        anonymous HTTP request, please pass asynchronous=True
        >>> thread = api.get_groups_of_account_user_with_http_info(account_id, user_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str account_id: Account ID. (required)
        :param str user_id: The ID of the user whose details are retrieved. (required)
        :param int limit: The number of results to return (2-1000), default is 50.
        :param str after: The entity ID to fetch after the given one.
        :param str order: The order of the records based on creation time, ASC or DESC; by default ASC
        :param str include: Comma separated additional data to return. Currently supported: total_count
        :return: GroupSummaryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'user_id', 'limit', 'after', 'order', 'include']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_
