def configure(self, mount_point, mfa_type='duo', force=False):
        """Configure MFA for a supported method.

        This endpoint allows you to turn on multi-factor authentication with a given backend.
        Currently only mfa is supported.

        Supported methods:
            POST: /auth/{mount_point}/mfa_config. Produces: 204 (empty body)

        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :param mfa_type: Enables MFA with given backend (available: duo)
        :type mfa_type: str | unicode
        :param force: If True, make the "mfa_config" request regardless of circumstance. If False (the default), verify
            the type mount_point is available and one of the types of authentication supported by this feature.
        :type force: bool
        :return: The response of the configure MFA request.
        :rtype: requests.Response
        """
        if force is False and mfa_type not in self.SUPPORTED_MFA_TYPES:
            error_msg = '"{0}" is not supported as an MFA type. Supported MFA types: {1}'.format(
                mfa_type, ', '.join(self.SUPPORTED_MFA_TYPES))
            raise exceptions.ParamValidationError(error_msg)

        api_path = utils.format_url('/v1/auth/{mount_point}/mfa_config', mount_point=mount_point)
        params = {'type': mfa_type}
        return self._adapter.post(
            url=api_path,
            json=params,
        )

