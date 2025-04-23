def _readReplacementFiles(self, directory, session, spatial, spatialReferenceID):
        """
        Check for the zero replacement file cards
        (REPLACE_PARAMS and REPLACE_VALS) and read the files into
        two if they exist.

        Returns:
            memory or None if it doesn't exist
        """
        replaceParamsFile = None
        replaceValsFile = None

        replaceParamsFileName = os.path.join(directory,'replace_params.txt')
        if os.path.exists(replaceParamsFileName):
            replaceParamsFile = _readReplaceFile(replaceParamsFileName, session, spatial, spatialReferenceID)

        replaceValsFileName = os.path.join(directory,'replace_vals.txt')
        if os.path.exists(replaceValsFileName):
            replaceValsFile = _readReplaceFile(replaceValsFileName, session, spatial, spatialReferenceID)

        return replaceParamsFile, replaceValsFile


