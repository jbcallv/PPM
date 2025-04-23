def read(self, directory, filename, session, spatial=False,
             spatialReferenceID=4236, replaceParamFile=None, **kwargs):
        """
        Generic read file into database method.

        Args:
            directory (str): Directory containing the file to be read.
            filename (str): Name of the file which will be read (e.g.: 'example.prj').
            session (:mod:`sqlalchemy.orm.session.Session`): SQLAlchemy session object bound to for enabled database.
            spatial (bool, optional): If True, spatially enabled objects will be read in as PostGIS spatial objects.
                Defaults to False.
            spatialReferenceID (int, optional): Integer id of spatial reference system for the model. Required if
                spatial is True. Defaults to srid 4236.
            replaceParamFile (:class:`gsshapy.orm.ReplaceParamFile`, optional): no instance. Use this if
                the file you are reading contains the parameters.
        """
        raise NotImplementedError

