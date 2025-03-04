def _convert_consonant(sign):
        """
        Uses characters to replace ATF input for unicode characters.

        characters = ['as,', 'S,ATU', 'tet,', 'T,et', 'sza', 'ASZ']
        output = ['aṣ', 'ṢATU', 'teṭ', 'Ṭet', 'ša', 'AŠ']

        :param sign: string
        :return: string
        """

        if sign in characters:
            return output[characters.index(sign)]
        else:
            return sign

