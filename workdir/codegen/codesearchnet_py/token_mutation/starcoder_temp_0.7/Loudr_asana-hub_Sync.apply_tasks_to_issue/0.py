def apply_tasks_to_issue(self, issue, tasks, issue_body=None):
        """Applies a only to an issue."""
        self._logger.debug("Applying tasks to issue %s", issue)
        issue_body = issue_body or issue.body
        for task in tasks:
            issue_body = task.apply(issue_body)
        self._logger.debug("Issue body after applying tasks: %s", issue_body)
        return issue_body

    def apply_tasks_to_repo(self, repo, tasks, branch=None, issue_body=None):
        """Applies a only to an repo."""
        for issue in repo.issues():
            self._logger.debug("Applying tasks to issue %s", issue)
            if issue_body is None:
                issue_body = issue.body
            for task in tasks:
                issue_body = task.apply(issue_body)
            self._logger.debug("Issue body after applying tasks: %s", issue_body)
            if branch is not None:
                issue.edit(body=issue_body, branch=branch)
            else:
                issue.edit(body=issue_body)

