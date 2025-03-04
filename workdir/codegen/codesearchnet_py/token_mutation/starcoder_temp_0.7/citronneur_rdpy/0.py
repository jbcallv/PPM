def expectWithHeader(self, expectedHeaderLen, callbackBody):
        """
        2nd level of waiting event
        read expectedHeaderLen that for body size
        @param expectedHeaderLen: contains the number of bytes, which body length needs to be encoded
        @param callbackBody: contains for use when expected date from expectedHeaderLen
        are received
        """
        self.read(length=expectedHeaderLen, expect=callbackBody)
