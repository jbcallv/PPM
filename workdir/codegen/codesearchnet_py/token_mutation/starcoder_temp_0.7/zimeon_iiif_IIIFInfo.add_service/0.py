def add_service(self, service):
        """Add a given description.

        " transition from self.service=None, self.service=dict for a
        service service, and then self.service=[dict,dict,...] for multiple
        """
        if self.service is None:
            self.service = service
        elif type(self.service) is list:
            self.service.append(service)
        else:
            self.service = [self.service, service]

