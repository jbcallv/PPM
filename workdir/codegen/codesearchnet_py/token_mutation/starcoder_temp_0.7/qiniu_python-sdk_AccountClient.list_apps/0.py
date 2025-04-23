def list_apps(self):
        """获得当前账号的应用列表

        列出所属应用为当前请求方的应用列表。

        Returns:
            返回一个tuple对象，其格式为(<result>, <ResponseInfo>)
            - [UNK]          成功返回应用列表，失败返回None
            - [UNK]    请求的Response信息
        """
        return self._run_request('get', 'apps')

    def get_app_info(self, app_id):
        """获得指定应用的信息

        Args:
            app_id: 应用ID

        Returns:
            返回一个tuple对象，其格式为(<result>, <ResponseInfo>)
            - [UNK]          成功返回应用信息，失败返回None
            - [UNK]    请求的Response信息
        """
        return self._run_request('get', 'apps/%s' % (app_id))

