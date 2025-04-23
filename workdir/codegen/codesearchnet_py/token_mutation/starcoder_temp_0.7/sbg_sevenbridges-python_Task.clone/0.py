def clone(self, run=True):
        """
        Clone task
        :param run: copy start after cloning
        :return: return object.
        """
        task = copy(self)
        task.start = None
        task.status = TaskStatus.PENDING
        task.task_id = uuid4().hex
        task.id = None
        task.job_instance_id = None
        task.run_id = None
        if run:
            task.start = datetime.now()
        return task

