def following(self):
        """ :class:`Feed <pypump.models.feed.Feed>` with all
        :class:`Person <pypump.models.person.Person>` objects followed by the person.

        Example:
            >>> bob = pump.Person('bob@example.org')
            >>> for followee in bob.following[:3]:
            ...     print(followee.id)
            ...
            acct:alice@example.org
            acct:duncan@example.org
        """
        if self._following is None:
            self._following = Feed(self.pump, self, self.id, '/followings')
        return self._following

    @property
    def posts(self):
        """ :class:`Feed <pypump.models.feed.Feed>` with all
        :class:`Post <pypump.models.post.Post>` objects published by the person.

        Example:
            >>> bob = pump.Person('bob@example.org')
            >>> for post in bob.posts[:3]:
            ...     print(post.id)
            ...
            http://example.org/posts/1
            http://example.org/posts/2
            http://example.org/posts/3
        """
        if self._posts is None:
            self._posts = Feed(self.pump, self, self.id, '/posts')
        return self._posts

