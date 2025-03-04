def update_package(self, package_version_details, feed_id, package_name, package_version):
        """UpdatePackage.
        [Preview API]
        :param :class:`<PackageVersionDetails> <azure.devops.v5_0.npm.models.PackageVersionDetails>` package_version_details:
        :param : feed_id:
        :param . package_name:
        :param : package_version:
        :rtype: :class:`<Package> <azure.devops.v5_0.npm.models.Package>`
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id,'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name,'str')
        query_parameters = {}
        if package_version is not None:
            query_parameters['packageVersion'] = self._serialize.query('package_version', package_version,'str')
        content = self._serialize.body(package_version_details, 'PackageVersionDetails')
        response = self._send(http_method='PATCH',
                              location_id='95029e0c-1057-4937-b46a-61621c67b984',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Package', response)

    def update_package_version_promotion_status(self, package_version_promote_details, feed_id, package_name, package_version):
        """UpdatePackageVersionPromotionStatus.
        [Preview API]
        :param :class:`<PackageVersionPromoteDetails> <azure.devops.v5_0.npm.models.PackageVersionPromoteDetails>` package_version_promote_details:
        :param : feed_id:
        :param . package_name:
        :param : package_version:
        :rtype: :class:`<Package> <azure.devops.v5_0.npm.models.Package>`
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id,'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name,'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version,'str')
        content = self._serialize.body(package_version_promote_details, 'PackageVersionPromoteDetails')
        response = self._send
