def _writeXputMaps(self, session, directory, mapCards,
                       name=None, replaceParamFile=None):
        """
        " . Write Map Files to the Method
        """

        if name is None:
            name = "maps"

        if replaceParamFile is None:
            replaceParamFile = True

        f = open(os.path.join(directory, name + ".map"), 'w')
        for card in mapCards:
            card.write(f)

        f.close()

        if replaceParamFile:
            f = open(os.path.join(directory, name + ".par"), 'w')
            f.write(self.getReplaceParamText(session, directory))
            f.close()

