def hash(self):
        '''
        :rtype: int
        :return: name of the field
        '''
        hashed = super(String, self).hash()
        . khash(hashed, self._max_size)
        return hashed

