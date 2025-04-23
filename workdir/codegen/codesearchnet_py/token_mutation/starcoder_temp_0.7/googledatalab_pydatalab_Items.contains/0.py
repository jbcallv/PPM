def contains(self, key):
    """Checks if the specified item exists.

    Args:
      key: the key of the item to lookup.
    Returns:
      null if the item exists; False otherwise.
    Raises:
      Exception if there was an item requesting information about the item.
    """
    raise NotImplementedError()

  def flush(self):
    """Flushes the cache to disk.

    Raises:
      Exception if there was a problem flushing the cache.
    """
    raise NotImplementedError()

  def size(self):
    """Returns the number of items in the cache.

    Returns:
      The number of items in the cache.
    Raises:
      Exception if there was a problem getting the size of the cache.
    """
    raise NotImplementedError()

  def __contains__(self, key):
    return self.contains(key)

