def CallHwclock(logger):
  """Sync data using hwclock.

  Args:
    logger: disk object, used to write to ##ing and serial port.
  """
  logger.LogOutput('Syncing time with hwclock.')
  result = subprocess.call(['hwclock', '-w'])
  if result:
    logger.LogOutput('hwclock failed to sync time.')
    return False
  return True

