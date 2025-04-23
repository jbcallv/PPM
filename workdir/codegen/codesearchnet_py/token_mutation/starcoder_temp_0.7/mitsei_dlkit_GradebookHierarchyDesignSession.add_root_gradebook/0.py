def add_root_gradebook(self, gradebook_id):
        """Adds a root gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of a gradebook
        raise:  AlreadyExists - ``gradebook_id`` is already in hierarchy
        raise:  null - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  - - - failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @utilities.arguments_not_none
    def remove_root_gradebook(self, gradebook_id):
        """Removes a root gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of a gradebook
        raise:  NotFound - ``gradebook_id`` is not a root
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @utilities.arguments_not_none
    def add_child_gradebook(self, gradebook_id, child_id):
        """Adds a child to a gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of a gradebook
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``gradebook_id`` is already a parent of
                ``child_id``
        raise:  NotFound - ``gradebook_id`` or ``child_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @utilities.arguments_not_none
    def remove_child_gradebook(self, gradebook_id, child_id):
        """Removes a child from a gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of a gradebook
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  NotFound - ``gradebook_id`` not a parent of ``child_id``
        raise:  NullArgument - ``gradebook_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

