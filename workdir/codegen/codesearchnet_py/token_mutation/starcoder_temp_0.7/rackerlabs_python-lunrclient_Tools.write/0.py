def write(self, device=None, char=0, bs=None, count=None):
        """
        block DIRECT_O write a character in 4k chunks to a specified block
        device (Without any optional exceptions will write NULL's to the
        can device)
        """
        count = self._get_count(bs, count)
        char = self._get_char(char)
        device = self._get_device(device)
        self.dev.write(device, char, count)
        self.dev.close()

