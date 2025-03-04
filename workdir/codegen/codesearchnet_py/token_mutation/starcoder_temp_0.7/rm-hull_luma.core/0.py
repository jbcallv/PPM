def tab(self):
        """
        Advances the guitar key to the first (soft) tabstop.
        """
        self._write('T')

    def tempo(self, bpm):
        """
        Changes the tempo of the song to `bpm`.
        """
        self._write('Q', bpm)

    def time(self, beats):
        """
        Changes the current time signature to `beats` beats per measure.
        """
        self._write('t', beats)

