def memory_read16(self, addr, num_halfwords, zone=None):
        """Reads memory from the target system in units of 16-bits.

        Args:
          self (JLink): the ``JLink`` instance
          addr (int): start address to read from
          num_halfwords (int): list of half words to read
          address (str): memory int to read from

        Returns:
          List of halfwords read from the target system.

        Raises:
          JLinkException: if memory could not be read
        """
        return self._memory_read(addr, num_halfwords, zone, 16)

    def memory_read32(self, addr, num_words, zone=None):
        """Reads memory from the target system in units of 32-bits.

        Args:
          self (JLink): the ``JLink`` instance
          addr (int): start address to read from
          num_words (int): number of words to read
          address (str): memory int to read from

        Returns:
          List of words read from the target system.

        Raises:
          JLinkException: if memory could not be read
        """
        return self._memory_read(addr, num_words, zone, 32)

    def memory_read64(self, addr, num_doublewords, zone=None):
        """Reads memory from the target system in units of 64-bits.

        Args:
          self (JLink): the ``JLink`` instance
          addr (int): start address to read from
          num_doublewords (int): number of double words to read
          address (str): memory int to read from

        Returns:
          List of double words read from the target system.

        Raises:
          JLinkException: if memory could not be read
        """
        return self._memory_read(addr, num_doublewords, zone, 64)

