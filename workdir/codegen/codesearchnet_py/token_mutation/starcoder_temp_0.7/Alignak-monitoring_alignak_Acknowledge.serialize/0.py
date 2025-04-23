def serialize(self):
        """This can serialize into a simple dict object.
        It is used when transferring end to other daemons over the network (http)

        Here we directly return all attributes

        :return: json data of a Acknowledge
        :rtype: dict
        """
        return self.__dict__

