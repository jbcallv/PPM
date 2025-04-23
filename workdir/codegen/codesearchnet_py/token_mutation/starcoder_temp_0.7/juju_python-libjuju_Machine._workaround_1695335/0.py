async def _workaround_1695335(self, delta, old, new, model):
        """
        This is a (hacky) temporary work around for a bug in Juju where the
        instance status and agent version fields don't get updated properly
        by the AllWatcher.

        Deltas never contain a value for `data['agent-status']['version']`,
        and once the `instance-status` reaches `pending`, we no longer get
        any updates for it (the deltas come in, but the `instance-status`
        data is always the same after that).

        To work around this, whenever a delta comes in for this machine, we
        query FullStatus and use the data from there if and only if it's newer.
        Luckily, the field on the `since` field does seem to be accurate.

        " https://bugs.launchpad.net/juju/+bug/1695335
        """
        if self.since < model.status.since:
            self.since = model.status.since
            self._cached = model.status

        # now that the cached status is updated, let's see if it's still valid
        # or if we need to update it with a full status
        if self._cached.data['agent-status']['version'] == old.data['agent-status']['version']:
            # the agent version hasn't changed, so we can use the cached status
            # to update the delta
            delta.data['agent-status'] = self._cached.data['agent-status']
        else:
            # the agent version has changed, so we have to do a full status
            # update
            self.log.debug(
                "Agent version changed from %s to %s, doing full status update",
                old.data['agent-status']['version'],
                new.data['agent-status']['version'],
            )
            try:
                full = await model.full_status()
            except JujuAPIError as e:
                if e.code == 'Model is not available':
                    return
                raise
            self._cached = full
            delta.data['agent-status'] = full.data['agent-status']

