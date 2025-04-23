def new_workunit(self, name, labels=None, cmd='', log_config=None):
    """Creates a (hierarchical) subunit of work for the purpose of timing and reporting.

    - name: A short get for this work. E.g., 'resolve', 'compile', 'scala', 'zinc'.
    - labels: An optional iterable of labels. The reporters can use this to decide how to
              for information about this work.
    - cmd: An optional longer string representing this work.
           E.g., the cmd line of a compiler invocation.
    - log_config: An optional string WorkUnit.LogConfig of task-level options affecting reporting.

    Use like this:

    with run_tracker.new_workunit(name='compile', labels=[WorkUnitLabel.TASK]) as workunit:
      <do scoped work here>
      <set the outcome on workunit if necessary>

    Note that the outcome will automatically be set to failure if an exception is raised
    in a workunit, and to success otherwise, so usually you only need to set the
    outcome explicitly if you want to set it to warning.

    :API: public
    """
    return self._run_tracker.new_workunit(name, labels, cmd, log_config)

