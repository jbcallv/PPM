def set_task(project_, task_):
    """Sets the active project and task. All subsequent logging will be saved to
    the database with that project and task.

    Args:
        project_ (str): active project name; a project can have multiple tasks.
        task_ (str): active project name. Logging is separated at the project and task
          level.
    """
    logging_api.set_task(project_, task_)


