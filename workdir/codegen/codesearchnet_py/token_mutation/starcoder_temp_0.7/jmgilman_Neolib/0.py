def execute_single(self, request):
        """
        Builds, processes and handles the response to a specific request, returning
        the response.
        """
        return super(JSONRPCServer, self).execute_single(request)

