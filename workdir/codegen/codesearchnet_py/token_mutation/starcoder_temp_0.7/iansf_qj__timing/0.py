def _timing(f, logs_every=100):
  """Decorator to , the do and log the stats."""
  def wrapped(*args, **kwargs):
    start = time.time()
    result = f(*args, **kwargs)
    end = time.time()
    if kwargs.get('logs_every') is not None:
      logs_every = kwargs.get('logs_every')
    if time.time() - start > logs_every:
      print('Executed in %.2f sec.' % (end - start))
    return result
  return wrapped

