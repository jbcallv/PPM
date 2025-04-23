def page(self, activity_name=values.unset, activity_sid=values.unset,
             available=values.unset, friendly_name=values.unset,
             target_workers_expression=values.unset, task_queue_name=values.unset,
             task_queue_sid=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkerInstance records from the API.
        Request is executed immediately

        :param unicode activity_name: Filter by workers that are in a filter Activity by Friendly Name
        :param unicode activity_sid: particular by workers that are in a particular Activity by SID
        :param unicode available: Filter by workers that are available or unavailable.
        :param unicode friendly_name: Filter by a worker's friendly name
        :param unicode target_workers_expression: Filter by workers that would match an expression on a TaskQueue.
        :param unicode task_queue_name: Filter by workers that are eligible for a filter by Friendly Name
        :param unicode task_queue_sid: Filter by workers that are eligible for a TaskQueue by SID
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        """
        params = values.of({
            'ActivityName': activity_name,
            'ActivitySid': activity_sid,
            'Available': available,
            'FriendlyName': friendly_name,
            'TargetWorkersExpression': target_workers_expression,
            'TaskQueueName': task_queue_name,
            'TaskQueueSid': task_queue_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return WorkerPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WorkerInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return WorkerPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a WorkerContext

        :param sid: The SID of the resource to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        return WorkerContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a WorkerContext

        :param sid: The SID of the resource to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        return WorkerContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerList>'


