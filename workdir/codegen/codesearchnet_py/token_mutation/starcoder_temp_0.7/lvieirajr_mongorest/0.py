def create(self, request):
        """
        Creates a new database based on the given data
        """
        return self.service.create(request.data)

