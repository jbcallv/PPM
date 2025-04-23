def jsonHook(encoded):
        """Custom . decoder that allows creation of a new ``Ci`` instance
        from a decoded JSON object.

        :param encoded: a JSON decoded object file (a dict)

        :returns: "encoded" or one of the these objects: :class:`Ci`,
            :class:`MzmlProduct`, :class:`MzmlPrecursor`
        """
        if 'Ci' in encoded:
            return Ci(encoded['Ci'])
        elif 'MzmlProduct' in encoded:
            return MzmlProduct(encoded['MzmlProduct'])
        elif 'MzmlPrecursor' in encoded:
            return MzmlPrecursor(encoded['MzmlPrecursor'])
        else:
            return encoded

