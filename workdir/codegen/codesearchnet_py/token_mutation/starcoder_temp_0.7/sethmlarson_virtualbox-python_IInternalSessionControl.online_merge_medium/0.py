def online_merge_medium(self, medium_attachment, source_idx, target_idx, progress):
        """Triggers online merging of a hard disk. Used internally when deleting
        a snapshot while a VM referring to the same hard disk chain is running.

        in medium_attachment of type :class:`IMediumAttachment`
            The medium attachment to identify the medium chain.

        in source_idx of type int
            The index of the source image in the chain.
            Redundant, but drastically reduces IPC.

        in target_idx of type int
            The index of the target image in the chain.
            Redundant, but drastically reduces IPC.

        in access of type :class:`IProgress`
            Progress object for this operation.

        raises :class:`VBoxErrorInvalidVmState`
            Machine session is not open.
        
        raises :class:`VBoxErrorInvalidObjectState`
            Session ##vocation is not direct.
        
        """
        return self._o.online_merge_medium(medium_attachment, source_idx, target_idx, progress)

    def get_medium(self, name_or_id, access_mode, device_type):
        """Returns the medium with the given name or UUID.

        in name_or_id of type unicode
            The name or UUID of the medium.

        in access_mode of type :class:`AccessMode`
            The access mode for the medium.

        in device_type of type :class:`DeviceType`
            The device type of the medium.

        returns :class:`IMedium`
            Medium object.

        raises :class:`VBoxErrorObjectNotFound`
            No medium with the given name or UUID.

        """
        return self._o.get_medium(name_or_id, access_mode, device_type)

    def get_medium_by_id(self, medium_id):
        """Returns the medium with the given UUID.

        in medium_id of type unicode
            The UUID of the medium.

        returns :class:`IMedium`
            Medium object.

        raises :class:`VBoxErrorObjectNotFound`
            No medium with the given UUID.

        """
        return self._o.get_medium_by_id(medium_id)

    def get_mediums_by_id(self, medium_ids):
        """Returns the mediums with the given UUIDs.

        in medium_ids of type [unicode]
            The UUIDs of the mediums.

        returns [:class:`IMedium`]
            Medium objects.

        raises :class:`VBoxErrorObjectNotFound`
            No medium with the given UUID.

        """
        return self._o.get_mediums_by_id(medium_ids)

    def get_mediums(self, access_mode, device_type):
        """Returns all media matching the given type.

        in access_mode of type :class:`AccessMode`
            The access mode for the medium.

        in device_type of type :class:`DeviceType`
            The device type of the medium.

        returns [:class:`IMedium`]
            Medium objects.

        """
        return self._o.get_mediums(access_mode, device_type)

    def get_dvds(self):
        """Returns all DVD images.

        returns [:class:`IMedium`]
            Medium objects.

        """
        return self._
