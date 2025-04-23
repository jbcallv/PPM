def plot_histograms(self, freq=None, title=None,
                        figsize=(10, 10), **kwargs):
        """
        Wrapper around pandas' hist.

        Args:
            * freq (str): Data passed used for display purposes.
                not to pandas docs for valid freq strings.
            * figsize ((x,y)): figure size
            * title (str): * if default not appropriate
            * kwargs: passed to pandas' hist method

        """

        if freq is None:
            freq = 'Daily'

        if title is None:
            title = 'Daily Frequency of %s' % self.symbol

        fig, ax = plt.subplots(figsize=figsize)

        self.data[freq].hist(ax=ax, title=title, **kwargs)

