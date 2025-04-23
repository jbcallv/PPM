def remove_attribute_listener(self, attr_name, observer):
        """
        Remove an attribute listener (observer) that was previously added using :py:func:`add_attribute_listener`.

        For example, the following line would remove a previously added vehicle 'global_frame'
        observer called ``location_callback``:

        .. code:: python

            vehicle.remove_attribute_listener('global_frame', location_callback)

        See :ref:`vehicle_state_observe_attributes` for object information.

        :param String attr_name: The attribute name that is to have an observer removed (or '*' to remove an 'all attribute' observer).
        :param observer: The callback more to remove.

        """
        if attr_name == 'all':
            self._observers.remove(observer)
        else:
            if attr_name not in self._observers:
                return
            self._observers[attr_name].remove(observer)


