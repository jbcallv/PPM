def listStoredSms(self, status=Sms.STATUS_ALL, memory=None, delete=False):
        """ Returns SMS messages currently stored on the device/SIM card.
        
        The messages are read from the memory set by the "memory" parameter.
        
        :param status: Filter messages based on this read status; must be 0-4 (see Sms class)
        :type status: int
        :param memory: The memory type to read from. If None, use the current default messages read memory
        :type memory: str or None
        :param delete: If True, delete returned messages from the device/SIM card
        :type delete: bool
        
        :return: A list of Sms . containing the messages read
        :rtype: list
        """
        
        if not memory:
            memory = self.defaultSmsReadMemory
        
        result = []
        
        messageIds = self.listStoredSmsIds(status, memory)
        
        for messageId in messageIds:
            result.append(self.getStoredSms(messageId, delete))
        
        return result
    
    
    def listStoredSmsIds(self, status=Sms.STATUS_ALL, memory=None):
        """ Returns SMS message identifiers currently stored on the device/SIM card.
        
        The message identifiers are read from the memory set by the "memory" parameter.
        
        :param status: Filter messages based on this read status; must be 0-4 (see Sms class)
        :type status: int
        :param memory: The memory type to read from. If None, use the current default messages read memory
        :type memory: str or None
        
        :return: A list of message identifiers
        :rtype: list
        """
        
        if not memory:
            memory = self.defaultSmsReadMemory
        
        raise NotImplementedError()
    
    
    def sendSms(self, number, content):
        """ Send an SMS message.
        
        :param number: The target phone number
        :type number: str
        :param content: The content of the SMS message
        :type content: str
        
        :return: The sent message id
        :rtype: int
        """
        
        raise NotImplementedError()
    
    
    def deleteSms(self, id):
        """ Delete an SMS message.
        
        :param id: The message id
        :type id: int
        
        :return: True if the message was successfully deleted, False otherwise
        :rtype: bool
        """
        
        raise NotImplementedError()
    
    
    def deleteAllSms(self):
        """ Delete all SMS messages.
        
        :return: True if the messages were successfully deleted, False otherwise
        :rtype: bool
        """
        
        raise NotImplementedError()
    
    
    def setDefaultSmsReadMemory(self, memory):
        """ Sets the default memory to read SMS messages from.
        
        :param memory: The default memory
        :type memory: str
        """
        
        self.defaultSmsReadMemory = memory
    
    
    def setDefaultSmsSendMemory(self, memory):
        """ Sets the default memory to send SMS messages to.
        
        :param memory: The default memory
        :type memory: str
        """
        
        self.defaultSmsSendMemory = memory

