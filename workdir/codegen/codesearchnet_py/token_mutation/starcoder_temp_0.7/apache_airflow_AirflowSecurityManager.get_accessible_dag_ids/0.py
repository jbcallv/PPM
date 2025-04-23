def get_accessible_dag_ids(self, username=None):
        """
        Return a set of dags that user has access to(either read or write).

        :param username: name of the user.
        :return: A set of dag files that the user could access.
        """<fim_suffix>           return []

        return self._get_dag_ids_user_has_access_to(
            username,
            dag_ids=dag_ids,
            permission_type=DagPermission.CAN_READ,
            session=session,
            include_children=include_children,
        )

    def _get_dag_ids_user_has_access_to(
        self,
        username,
        dag_ids=None,
        permission_type=None,
        session=None,
        include_children=True,
    ):
        """
        Get list of DAGs that the user has access to(either read or write).
        """
        if not dag_ids:
            dag_ids = self.get_accessible_dag_ids(username, session=session)

        dag_ids_to_filter = dag_ids
        if not include_children:
            dag_ids_to_filter = [dag_id for dag_id in dag_ids if not dag_id.count(".")]

        query = (
            session.query(cls.dag_id)
           .filter(
                cls.dag_id.in_(dag_ids_to_filter),
                cls.user_id == username,
                cls.permission == permission_type,
            )
           .distinct()
        )

        return {dag_id[0] for dag_id in query}

    def _get_dag_ids_user_can_dag_read(self, dag_ids, session=None, include_children=True):
        """
        Get list of DAGs that the user can read
        """
        return self._get_dag_ids_user_has_access_to(
            username=current_user.username,
            dag_ids=dag_ids,
            permission_type=DagPermission.CAN_READ,
            session=session,
            include_children=include_children,
        )

    def _get_dag_ids_user_can_dag_edit(self, dag_ids, session=None, include_children=True):
        """
        Get list of DAGs that the user can edit
        """
        return self._get_dag_ids_user_has_access_to(
            username=current_user.username,
            dag_ids=dag_ids,
            permission_type=DagPermission.CAN_EDIT,
            session=session,
            include_children=include_children,
