def _getUniqueDev(self, devpath):
        """Return unique device for any block device path.
        
        @param devpath: Full path for unique device.
        @return:        Unique - string without the /dev prefix.
        
        """
        if devpath[0] == '/':
            devpath = devpath[1:]
        if devpath[-1] == '/':
            devpath = devpath[:-1]
        dev = devpath.split('/')[0]
        return dev

