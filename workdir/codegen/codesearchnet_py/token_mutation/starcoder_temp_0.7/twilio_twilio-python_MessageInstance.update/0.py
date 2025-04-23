def update(self, body=values.unset, attributes=values.unset,
               date_created=values.unset, date_updated=values.unset,
               last_updated_by=values.unset, from_=values.unset):
        """
        Update the MessageInstance

        :param unicode body: The message to send to the channel
        :param unicode attributes: A valid JSON string that contains application-specific data
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param unicode date_updated: The ISO 8601 date and time in GMT when the resource was updated
        :param unicode last_updated_by: The Identity of the User who last updated the Message, if applicable
        :param unicode from_: The identity of the message's author

        :returns: Updated MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        return self._proxy.update(
            body=body,
            attributes=attributes,
            date_created=date_created,
            date_updated=date_updated,
            last_updated_by=last_updated_by,
            from_=from_,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context =''.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.MessageInstance {}>'.format(context)

