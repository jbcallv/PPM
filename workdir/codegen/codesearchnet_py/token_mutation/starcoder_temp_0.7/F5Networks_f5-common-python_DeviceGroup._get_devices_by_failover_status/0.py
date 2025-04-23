def _get_devices_by_failover_status(self, status):
        '''Get a list of bigips by failover status.

        :param status: ' -- status to filter the returned list of devices
        :returns: returns -- list of devices that have the given status
        '''

        devices_with_status = []
        for device in self.devices:
            if (self._check_device_failover_status(device, status)):
                devices_with_status.append(device)
        return devices_with_status

