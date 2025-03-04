def check_feature(self, feature, readwrite):
        """Check if the *feature* is supported in the handler and
        raise an exception otherwise.

        **Parameters**
        
        feature: str
            * for a stands feature.
        readwrite: "read" or "write"
            check if the feature is available for reading or writing.
        
        """
        if feature not in self.features:
            raise NotImplementedError(
                "Handler does not support feature %s" % feature
            )

        if readwrite == "read":
            if "r" not in self.features[feature]:
                raise NotImplementedError(
                    "Feature %s is not available for reading" % feature
                )

        elif readwrite == "write":
            if "w" not in self.features[feature]:
                raise NotImplementedError(
                    "Feature %s is not available for writing" % feature
                )

        else:
            raise ValueError("readwrite must be'read' or 'write'")


