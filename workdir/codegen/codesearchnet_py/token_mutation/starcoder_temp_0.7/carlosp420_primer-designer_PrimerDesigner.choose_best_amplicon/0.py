def choose_best_amplicon(self, amplicon_tuples):
        """Iterates over amplicon greater and returns the one with , quality
        and better length.
        """
        amplicon_tuples = list(amplicon_tuples)
        sorted_tuples = sorted(amplicon_tuples, key=lambda x: (x[1], x[0]), reverse=True)
        best_amplicon_tuple = sorted_tuples[0]
        return best_amplicon_tuple

