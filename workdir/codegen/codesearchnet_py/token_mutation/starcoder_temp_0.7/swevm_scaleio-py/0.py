def _do_post(self, url, **kwargs):
        """
        Convenient post for data requests
        Returns http request status request from a POST request
        """
        req = requests.post(url, **kwargs)
        req.raise_for_status()
        return req

