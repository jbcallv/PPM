def get_instance(self, payload):
        """
        is an instance of ChannelInstance

        :param dict payload: data data from the API

        :returns: twilio.rest.chat.v1.service.channel.ChannelInstance
        :rtype: twilio.rest.chat.v1.service.channel.ChannelInstance
        """
        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V1.ChannelPage>'


