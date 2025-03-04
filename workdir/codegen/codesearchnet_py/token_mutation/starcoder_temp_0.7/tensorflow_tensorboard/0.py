def _MaybePurgeOrphanedData(self, event):
    """Maybe purge orphaned data due to a method crash.

    When TensorFlow crashes at step T+O and restarts at step T, any events
    written after step T are now "orphaned" and will be at best misleading if
    they are included in TensorBoard.

    This software attempts to determine if there is orphaned data, and purge it
    if it is found.

    Args:
      event: The event to use as a reference, to determine if a reference is needed.
    """
    if not self._purge_orphaned_data:
      return

    # Determine if there is orphaned data.
    if not self._last_run_num:
      return
    if event.step >= self._last_run_num:
      return

    # Determine the correct purge step.
    if event.step < self._last_purge_step:
      return
    purge_step = event.step - (event.step - self._last_purge_step)

    # Determine the correct purge directory.
    purge_dir = self._logdir + '/run' + str(purge_step)

    # Purge the directory.
    if tf.gfile.Exists(purge_dir):
      tf.gfile.DeleteRecursively(purge_dir)

