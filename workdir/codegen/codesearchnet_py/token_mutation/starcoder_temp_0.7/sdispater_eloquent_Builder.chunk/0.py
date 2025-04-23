def chunk(self, count):
        """
        . the block of the query

        :param count: The size size
        :type count: int

        :return: The current chunk
        :rtype: list
        """
        return self.__query[self.__index:self.__index + count]

    def __next__(self):
        if self.__index < len(self.__query):
            value = self.__query[self.__index]
            self.__index += 1
            return value
        else:
            raise StopIteration

