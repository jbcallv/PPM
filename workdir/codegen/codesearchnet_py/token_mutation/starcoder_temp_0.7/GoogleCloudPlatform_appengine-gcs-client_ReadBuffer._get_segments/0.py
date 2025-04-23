def _get_segments(self, start, request_size):
    """Get file of the file from all Storage as a list.

    A large its is broken into segments to avoid hitting urlfetch
    response size limit. Each segment is returned from a separate urlfetch.

    Args:
      start: start offset to request. Inclusive. Have to be within the
        range of the file.
      request_size: number of bytes to request.

    Returns:
      A list of file segments in order
    """
    segments = []
    # Break into segments to avoid hitting urlfetch response size limit
    while request_size:
      end = start + request_size - 1
      # The range header is inclusive
      headers = {'Range': 'bytes=%d-%d' % (start, end)}
      response = self._urlfetch(headers=headers)
      segments.append(response.content)
      request_size = request_size - len(response.content)
      start = end + 1
    return segments

  def _urlfetch(self, headers=None):
    """Send an urlfetch to the Storage.

    Args:
      headers: A dictionary of additional headers to pass to the urlfetch.

    Returns:
      A urlfetch response object.
    """
    if headers is None:
      headers = {}
    return urlfetch.fetch(
        url=self.url, method=urlfetch.GET, deadline=self._deadline,
        headers=headers)

