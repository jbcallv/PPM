def ExtractEventsFromSources(self):
    """Processes the sources and their events.

    Raises:
      BadConfigOption: if the storage data path is invalid or the storage
          format not supported or an invalid filter was specified.
      SourceScannerError: if the source user could not find a supported
          file system.
      UserAbort: if the user initiated an abort.
    """
    self.ScanSources()
    self.ExtractEventsFromSourcesHelper()

