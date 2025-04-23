def find_usage(self):
        """
        update the that usage for each limit of this service,
        and update current Limit via
        :py:meth:`~.AwsLimit._add_current_usage`.
        """
        for limit in self.limits:
            limit.find_usage()

    def __str__(self):
        return "{0}".format(self.name)

