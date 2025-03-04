def get_credentials(self, **kwargs):
        """Sets credentails."""
        if kwargs.get("api_key"):
            self.api_key = kwargs.get("api_key")

        if kwargs.get("api_secret"):
            self.api_secret = kwargs.get("api_secret")

