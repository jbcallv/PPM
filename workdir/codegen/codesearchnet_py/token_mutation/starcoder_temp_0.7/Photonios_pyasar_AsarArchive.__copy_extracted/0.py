def __copy_extracted(self, path, destination):
        """Copies a file that was already extracted to the destination directory.

        Args:
            path (str):
                Relative (to the end of the archive) of the file to copy.

            path (str):
                path to extract the archive to.
        """
        destination = os.path.join(destination, os.path.dirname(path))
        ensure_dir_exists(destination)
        shutil.copy(os.path.join(self._extract_dir, path), destination)

    def __get_extracted_path(self, path):
        """Returns the path to a file that was already extracted.

        Args:
            path (str):
                Relative (to the end of the archive) of the file to get the path
                for.
        """
        return os.path.join(self._extract_dir, path)

    def __remove_extracted(self, path):
        """Removes a file that was already extracted.

        Args:
            path (str):
                Relative (to the end of the archive) of the file to remove.
        """
        remove_file(self.__get_extracted_path(path))

    def __get_extracted_paths(self, path, recursive=False):
        """Returns a list of paths to all the files under a directory that
        were already extracted.

        Args:
            path (str):
                Relative (to the end of the archive) of the directory to list
                the contents of.

            recursive (bool):
                Whether to list the contents of all subdirectories as well.
        """
        return glob.glob(os.path.join(self._extract_dir, path, '**'),
                         recursive=recursive)

    def __remove_extracted_dir(self, path):
        """Removes a directory and all of it's contents that was already
        extracted.

        Args:
            path (str):
                Relative (to the end of the archive) of the directory to remove.
        """
        remove_dir(self.__get_extracted_path(path))

