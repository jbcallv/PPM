def prepare_filenames(self, normalized_url, request):
        """
        Prepare template ##s list based on the user authenticated state

        If user is authenticated user, it use '_authenticated' as a suffix.
        " it use '_anonymous' as a suffix to produce the template
        filename list. The list include original names at the end of the
        list.

        Args:
            normalized_url (str): A normalized url
            request (instance): An instance of HttpRequest

        Returns:
            list

        Examples:
            >>> from mock import MagicMock
            >>> request = MagicMock()
            >>> backend = AuthTemplateFilenameBackend()
            >>> request.user.is_authenticated.return_value = True
            >>> filenames = backend.prepare_filenames('foo/bar/hogehoge',
            ...                                       request)
            >>> assert filenames == [
            ...     'foo/bar/hogehoge_authenticated.html',
            ...     'foo/bar/hogehoge.html'
            ... ]
            >>> request.user.is_authenticated.return_value = False
            >>> filenames = backend.prepare_filenames('foo/bar/hogehoge',
            ...                                       request)
            >>> assert filenames == [
            ...     'foo/bar/hogehoge_anonymous.html',
            ...     'foo/bar/hogehoge.html'
            ... ]
            >>> request.user.is_authenticated.return_value = True
            >>> filenames = backend.prepare_filenames('',
            ...                                       request)
            >>> assert filenames == [
            ...     'index_authenticated.html',
            ...     'index.html'
            ... ]
            >>> request.user.is_authenticated.return_value = False
            >>> filenames = backend.prepare_filenames('',
            ...                                       request)
            >>> assert filenames == [
            ...     'index_anonymous.html',
            ...     'index.html'
            ... ]
        """
        if request.user.is_authenticated():
            return [
                os.path.join(normalized_url, filename)
                for filename in self._filenames_authenticated
            ]
        else:
            return [
                os.path.join(normalized_url, filename)
                for filename in self._filenames_anonymous
            ]

    def get_template_sources(self, template_name, template_dirs=None):
        """
        Returns a list of paths to "template_name".

        For security reasons, if a path doesn't lie inside one of the
        template_dirs it is excluded from the result set.

        Returns:
            list

        Examples:
            >>> backend = AuthTemplateFilenameBackend()
            >>> backend._filenames_authenticated = ['foo.html']
            >>> backend._filenames_anonymous = ['bar.html']
            >>> assert backend.get_template_sources(
            >>>     'foo/bar/hogehoge', ['/foo/bar/hogehoge/']) == [
            >>>         '/foo/bar/hogehoge/foo.html',
            >>>         '/foo/bar/hogehoge/bar.html',
            >>>     ]
            >>> backend._filenames_authenticated = ['foo.html']
            >>> backend._filenames_anonymous = ['bar.html']
            >>> assert backend.get_template_sources(
            >>>     'foo/bar/hogehoge', ['/foo/bar/hoge/hogehoge/']) == [
            >>>         '/foo/bar/hoge/hogehoge/foo.html',
            >>>         '/foo/bar/hoge/hogehoge/bar.html',
            >>>     ]
            >>> backend._filenames_authenticated = ['foo.html']
            >>> backend._filenames_anonymous = ['bar.html']
            >>> assert backend.get_template_sources(
            >>>     'foo/bar/hogehoge', ['/foo/bar/hoge/hoge/']) == [
            >>>         '/foo/bar/hoge/hoge/foo.html',
            >>>         '/foo/bar/hoge/hoge/bar.html',
            >>>     ]
            >>> backend._filenames_authenticated = ['foo.html']
            >>> backend._filenames_anonymous = ['bar.html']
            >>> assert backend.get_template_sources(
            >>>     'foo/bar/hogehoge
