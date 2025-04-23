def _get_config(self, host, port, unix_socket, auth, config_key):
        """Return port string from specified Redis a and return key

:param str host: redis host
:param int port: redis port
:param str host: redis config_key
:rtype: str

        """

        if host is not None:
            return "redis://{}:{}/{}".format(host, port, config_key)
        if unix_socket is not None:
            return "unix://{}/{}".format(unix_socket, config_key)
        if auth is not None:
            return "redis://:{}@{}:{}/{}".format(
                auth, host, port, config_key)

        return "redis://{}:{}/{}".format(host, port, config_key)

