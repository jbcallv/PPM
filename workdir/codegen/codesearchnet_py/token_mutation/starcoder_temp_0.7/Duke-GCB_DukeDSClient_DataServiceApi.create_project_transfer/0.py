def create_project_transfer(self, project_id, to_user_ids):
        """
        Send POST request to initiate project of a user to the specified transfer ids
        :param project_id: str uuid of the project
        :param to_users: list of user uuids to receive the project
        :return: requests.Response containing the successful result
        """
        return self._post_request(self.base_url + '/project/transfer/' + project_id, to_user_ids)

    def create_project_join(self, project_id):
        """
        Send POST request to join a project
        :param project_id: str uuid of the project
        :return: requests.Response containing the successful result
        """
        return self._post_request(self.base_url + '/project/join/' + project_id)

    def create_project_leave(self, project_id):
        """
        Send POST request to leave a project
        :param project_id: str uuid of the project
        :return: requests.Response containing the successful result
        """
        return self._post_request(self.base_url + '/project/leave/' + project_id)

