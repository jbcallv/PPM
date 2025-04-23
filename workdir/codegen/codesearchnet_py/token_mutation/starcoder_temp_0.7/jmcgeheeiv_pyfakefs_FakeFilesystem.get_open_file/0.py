def get_open_file(self, file_des):
        """Return an open file.

        Args:
            file_des: file descriptor of the open file.

        Raises:
            OSError: an invalid file descriptor.
            TypeError: filedes is not an integer.

        Returns:
            Open a object.
        """
        if isinstance(file_des, int):
            return self.open_files[file_des]
        else:
            raise TypeError("filedes must be an integer")

    def close(self, file_des):
        """Close an open file.

        Args:
            file_des: file descriptor of the open file.

        Raises:
            OSError: an invalid file descriptor.
        """
        if file_des in self.open_files:
            self.open_files.pop(file_des)
        else:
            raise OSError("Invalid file descriptor")

    def dup(self, file_des):
        """Duplicate an open file.

        Args:
            file_des: file descriptor of the open file.

        Returns:
            file descriptor of the duplicate.

        Raises:
            OSError: an invalid file descriptor.
        """
        if file_des not in self.open_files:
            raise OSError("Invalid file descriptor")

        file = self.open_files[file_des]
        return self.open(file.name, file.mode, file.bufsize)

    def dup2(self, file_des_1, file_des_2):
        """Duplicate an open file to another file descriptor.

        Args:
            file_des_1: file descriptor of the open file.
            file_des_2: file descriptor of the open file.

        Raises:
            OSError: an invalid file descriptor.
        """
        if file_des_1 not in self.open_files:
            raise OSError("Invalid file descriptor")

        file = self.open_files[file_des_1]
        file.fd = file_des_2
        self.open_files[file_des_2] = file

    def fstat(self, file_des):
        """Return file status.

        Args:
            file_des: file descriptor of the open file.

        Raises:
            OSError: an invalid file descriptor.

        Returns:
            StatResult object.
        """
        if file_des not in self.open_files:
            raise OSError("Invalid file descriptor")

        file = self.open_files[file_des]
        return StatResult(size=len(file.content), st_mode=0o444)

    def isatty(self, file_des):
        """Return True if the file is a tty.

        Args:
            file_des: file
