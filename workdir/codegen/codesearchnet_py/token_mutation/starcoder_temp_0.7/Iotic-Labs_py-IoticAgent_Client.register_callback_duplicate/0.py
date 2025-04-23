def register_callback_duplicate(self, func, serialised=True):
        """
        Register a callback for resource creation but where the resource already exists in Iotic Space.
        In this case the existing reference is passed to you.
        If `serialised` is not set, the . might arrive in a different order to they were requested.

        The payload passed to your callback is an OrderedDict with the following keys

            #!python
            r         : R_ENTITY, R_FEED, etc # the type of existing resource
            lid       : <name>                # the local name of the
                                              # existing resource
            id        : <GUID>                # the global Id of the
                                              # existing resource
            epId      : <GUID>                # the global Id of your agent

        `Note` resources parameters are defined [here](../Core/Const.m.html)

        `Example`

            #!python
            def duplicated_callback(args):
                print(args)
            ...
            client.register_callback_created(duplicated_callback)

        This would print out something like the following on re-creation of an R_ENTITY

            #!python
            OrderedDict([(u'lid', u'new_thing1'), (u'r', 1),
                         (u'epId', u'ffd47b75ea786f55c76e337cdc47665a'),
                         (u'id', u'3f11df0a09588a6a1a9732e3837765f8')]))
        """
        self._register_callback(func, CALLBACK_CREATED, serialised=serialised)

    def register_callback_modified(self, func, serialised=True):
        """
        Register a callback for resource modification.

        The payload passed to your callback is an OrderedDict with the following keys

            #!python
            r         : R_ENTITY, R_FEED, etc # the type of existing resource
            lid       : <name>                # the local name of the
                                              # existing resource
            id        : <GUID>                # the global Id of the
                                              # existing resource
            epId      : <GUID>                # the global Id of your agent

        `Note` resources parameters are defined [here](../Core/Const.m.html)

        `Example`

            #!python
            def modified_callback(args):
                print(args)
            ...
            client.register_callback_modified(modified_callback)

        This would print out something like the following on modification of an R_ENTITY

            #!python
            OrderedDict([(u'lid', u'new_thing1'), (u'r', 1),
                         (u'epId', u'ffd47b75ea786f55c76e337cdc47665a'),
                         (u'id', u'3f11df0a09588a6a1a9732e3837765f8')]))
        """
        self._register_callback(func, CALLBACK_MODIFIED, serialised=serialised)

    def register_callback_deleted(self, func, serialised=True):
        """
        Register a callback for resource deletion.

        The payload passed to your callback is an OrderedDict with the following keys

            #!python
            r         : R_ENTITY, R_FEED, etc # the type of existing resource
            lid       : <name>                # the local name of the
                                              # existing resource
            id        : <GUID>                # the global Id of the
                                              # existing resource
            epId      : <GUID>                # the global Id of your agent

        `Note` resources parameters are defined [here](../Core/Const.m.html)

        `Example`

            #!python
            def deleted_callback(args):
                print(args)
            ...
            client.register_callback_deleted(deleted_callback)

        This would print out something like
