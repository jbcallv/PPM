def _findExtnames(self, extname=None, exclude=None):
        """ This method builds a list of all functions which have 'EXTNAME'==extname
            and do not include any elements with 'EXTNAME'==exclude, if any are
            specified for exclusion at all.
        """
        extnames = []
        if extname is None:
            extname = 'SCI'
        for f in self.hdulist[1:]:
            if f.name.find('SCI') < 0:
                continue
            if exclude is not None and f.header.get('EXTNAME') == exclude:
                continue
            if f.header.get('EXTNAME') == extname:
                extnames.append(f.name)
        return extnames

