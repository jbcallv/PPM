def _set_attrs_to_values(self, response={}):
        """
        assigns attributes to dictionary values.

        - e.g.
        >>> import tmdbsimple as tmdb
        >>> movie = tmdb.Movies(103332)
        >>> response = movie.info()
        >>> movie.title  # instead of response['title']
        """
        for k, v in response.items():
            setattr(self, k, v)

