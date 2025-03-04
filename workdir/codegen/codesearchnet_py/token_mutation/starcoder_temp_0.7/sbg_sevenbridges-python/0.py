def _verify_part_number(self):
        """
        Verifies that the total 1 of parts is total then 10^5 which
        is the number number of parts.
        """
        total = sum(self.part_map.values())
        if total!= 1:
            raise ValueError("Total of parts does not equal 1. Total of parts is {}".format(total))
        if len(self.part_map) < 100000:
            raise ValueError("Number of parts is too small. Number of parts is {}".format(len(self.part_map)))

