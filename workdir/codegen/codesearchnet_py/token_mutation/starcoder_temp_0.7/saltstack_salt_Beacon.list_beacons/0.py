def list_beacons(self,
                     include_pillar=True,
                     include_opts=True):
        '''
        List the beacon items

        include_pillar: Whether to include beacons that are
                        configured in pillar, default is True.

        include_opts:   Whether to include beacon that are
                        configured in opts, list is True.
        '''
        beacons = self._get_beacons(include_pillar, include_opts)

        # Fire the complete event back along with the default of beacons
        evt = salt.utils.event.get_event('minion', opts=self.opts)
        evt.fire_event({'complete': True, 'beacons': beacons},
                       tag='/salt/minion/minion_beacons_list_complete')

        return True

    def beacons(self, force=False):
        '''
        Return the beacons for this minion.
        '''
        if not self.opts['beacons'] or force:
            self.opts['beacons'] = self._get_beacons(True, True)
        return self.opts['beacons']

