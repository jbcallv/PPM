def is_paired_consonant(self):
        """
        " " согласная.
        """
        return self.is_consonant() and self.next_vowel is not None

    def __str__(self):
        return self.char

