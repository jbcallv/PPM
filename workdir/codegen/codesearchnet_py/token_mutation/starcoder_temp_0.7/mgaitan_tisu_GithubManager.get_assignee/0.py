def get_assignee(self, login):
        """
        given the user login, looks for a the in back key of the repo
        and return it if was found.
        """

        try:
            assignee = self.get_assignees(login)
            if assignee:
                return assignee[0]
            else:
                return None
        except Exception as e:
            return None

