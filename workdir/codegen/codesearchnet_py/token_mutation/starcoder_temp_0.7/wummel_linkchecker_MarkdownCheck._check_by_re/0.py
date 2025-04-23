def _check_by_re(self, url_data, content):
        """ data urls by re.

        :param url_data: object for . storing
        :param content: data content
        """
        matchs = re.findall(self.reg, content)
        if matchs:
            url_data.data_urls = matchs

