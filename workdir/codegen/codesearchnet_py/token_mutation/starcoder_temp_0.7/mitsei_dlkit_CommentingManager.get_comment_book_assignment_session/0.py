def get_comment_book_assignment_session(self):
        """Gets the session for assigning comment to book mappings.

        return: (osid.commenting.CommentBookAssignmentSession) - a
                ``CommentBookAssignmentSession``
        raise:  - - unable to complete request
        raise:  Unimplemented - ``supports_comment_book_assignment()``
                is ``false``
        *compliance: * -- This procedure must be implemented if
        ``supports_comment_book_assignment()`` is ``true``.*

        """
        if not self.supports_comment_book_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CommentBookAssignmentSession(runtime=self._runtime)

    comment_book_assignment_session = property(fget=get_comment_book_assignment_session)

    def get_comment_book_assignment_session_for_book(self, book_id=None):
        """Gets the session for assigning comment to book mappings for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentBookAssignmentSession) - a
                ``CommentBookAssignmentSession``
        raise:  NotFound - ``book_id`` not found
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_book_assignment()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: * -- This procedure must be implemented if
        ``supports_comment_book_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_comment_book_assignment():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.CommentBookAssignmentSession(book_id, runtime=self._runtime)

    def get_book_lookup_session(self):
        """Gets the ``OsidSession`` associated with the book lookup service.

        return: (osid.commenting.BookLookupSession) - a
                ``BookLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_lookup()`` is ``false``
        *compliance: * -- This session must be implemented if
        ``supports_book_lookup()`` is ``true``.*

        """
        if not self.supports_book_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookLookupSession(runtime=self._runtime)

    book_lookup_session = property(fget=get_book_lookup_session)

    def get_book_query_session(self):
       
