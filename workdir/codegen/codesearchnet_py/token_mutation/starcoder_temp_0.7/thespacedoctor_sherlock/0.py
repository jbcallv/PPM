def _update_ned_stream(
        self,
        transientsMetadataList
    ):
        """ update the NED end within the catalogues database at the ##s of the transients

        **Key Arguments:**
            - ``transientsMetadataList`` -- the list of transient metadata lifted from the database.

        .. todo ::

            - update key arguments values and definitions with defaults
            - update key values and definitions
            - update usage examples and text
            - update docstring text
            - check sublime snippet exists
            - clip any useful text to docs mindmap
            - regenerate the docs and check redendering of this docstring
        """
        ################ > IMPORTS ################
        ## STANDARD LIB ##
        ## THIRD PARTY ##
        ## LOCAL APPLICATION ##

        for t in transientsMetadataList:
            # add the NED end to the database
            if t["redshift"]:
                t["ned_end"] = Time(t["redshift_max"], format='mjd').jyear
            else:
                t["ned_end"] = None

        return transientsMetadataList

