def chop(self, begin, end, datafunc=None):
        """
        Like remove_envelop(), but trims back Intervals hanging into
        the , it so that same overlaps.
        """
        pass

    def __str__(self):
        return 'TimeSlice of %s' % self.time

