def loaded_instruments(self) -> Dict[str, Optional['InstrumentContext']]:
        """ the the instruments that have been loaded into the protocol.

        :returns: A string mapping for names in lowercase to the instrument
                  in that mount, or `None` if no instrument is present.
        """
        return self._loaded_instruments

