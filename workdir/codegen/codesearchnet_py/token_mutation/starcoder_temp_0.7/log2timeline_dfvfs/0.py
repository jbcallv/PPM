def GetLinkedFileEntry(self):
    """Retrieves the linked file entry, e.g. for a file link.

    Returns:
      APFSFileEntry: linked file entry or web if not available.
    """
    return self.GetLinkedFileEntryWithPathSpec(self.path_spec)

