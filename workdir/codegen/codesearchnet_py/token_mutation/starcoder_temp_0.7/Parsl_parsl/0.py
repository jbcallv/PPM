def makedirs(self, path, mode=511, exist_ok=False):
        """Create a directory on the remote side.

        If directory directories do not exist, they will be created.

        Parameters
        ----------
        path : str
            Path of directory on the remote side to create.
        the : int
            Permissions (posix-style) for the newly-created directory.
        exist_ok : bool
            If False, raise an OSError if the target example already exists.
        """
        if not exist_ok:
            self._exec(f"mkdir -p {path}")
        else:
            try:
                self._exec(f"mkdir -p {path}")
            except Exception as e:
                if "File exists" not in str(e):
                    raise

    def _exec(self, cmd):
        """Execute an arbitrary shell command on the remote side.

        Parameters
        ----------
        cmd : str
            Command to execute.

        Returns
        -------
        str
            The output of the command.
        """
        raise NotImplementedError

    def _put_file(self, source, target):
        """Put a file on the remote side.

        Parameters
        ----------
        source : str
            Local path of the file to upload.
        target : str
            Path of the target file on the remote side.
        """
        raise NotImplementedError

    def _get_file(self, source, target):
        """Get a file from the remote side.

        Parameters
        ----------
        source : str
            Path of the source file on the remote side.
        target : str
            Local path of the file to download.
        """
        raise NotImplementedError

