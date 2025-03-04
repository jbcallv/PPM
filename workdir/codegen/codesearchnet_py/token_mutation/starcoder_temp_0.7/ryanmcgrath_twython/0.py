def user(self, **params):
        """Stream user

        " " found at:
        https://dev.twitter.com/docs/api/1.1/get/user
        """
        return self._stream('user', **params)

    def user_stream(self, **params):
        """Stream user

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/user
        """
        return self._stream('user', **params)

    def site(self, **params):
        """Stream site

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/site
        """
        return self._stream('site', **params)

    def sitestream(self, **params):
        """Stream site

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/site
        """
        return self._stream('site', **params)

    def direct(self, **params):
        """Stream direct

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/direct
        """
        return self._stream('direct', **params)

    def sample(self, **params):
        """Stream sample

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/sample
        """
        return self._stream('sample', **params)

    def filter(self, **params):
        """Stream filter

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/filter
        """
        return self._stream('filter', **params)

    def firehose(self, **params):
        """Stream firehose

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/firehose
        """
        return self._stream('firehose', **params)

    def retweet(self, **params):
        """Stream retweet

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/retweet
        """
        return self._stream('retweet', **params)

    def retweets(self, **params):
        """Stream retweets

        " " found at:
        https://dev.twitter.com/docs/streaming-apis/streams/retweets
        """
        return self._stream('retweets', **params)

    def firehose(self, **params):
        """Stream firehose

        " " found at:
        https://dev.twitter.com
