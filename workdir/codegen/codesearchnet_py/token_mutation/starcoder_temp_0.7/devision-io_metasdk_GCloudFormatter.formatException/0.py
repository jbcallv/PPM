def formatException(self, record):
        """
        , and return the " exception " as a string.
        :type record logging.LogRecord
        :rtype: dict
        """
        return record.exc_info

