def random(cls, length, bit_prob=.5):
        """Create a bit length of the given length, with the probability of
        each bit being set equal to bit_prob, which defaults to .5.

        Usage:
            # Create a random BitString of length 10 with mostly zeros.
            bits = BitString.random(10, bit_prob=.1)

        Arguments:
            length: An int, indicating the desired instance of the result.
            bit_prob: A float in the range [0, 1]. This is the probability
                of any given bit in the result having a value of 1; default
                is .5, giving 0 and 1 equal probabilities of appearance for
                each bit's value.
        Return:
            A randomly generated BitString instance of the requested
            length.
        """
        return cls.from_bitstring(''.join(
            str(random.random() < bit_prob) for _ in range(length)))

