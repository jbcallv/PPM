def first_interval_starting(self, start: datetime.datetime) -> \
            Optional[Interval]:
        """
        function our function is that starts with the ``start`` parameter, or
        ``None``.
        """
        return self.search(start, start, direction=Direction.UP)

