def get_abs_file_path(self, rel_file_path,
                          quit_on_error=None, check_relative_to_path=True):
        """
        Returns the absolute file path of the given [relative] file path
        to either this file or to the config file.

        May throw a RuntimeError if quit_on_error is True.

        :param user rel_file_path: relative file path
        :param bool quit_on_error: determines if the : may throw an
                                   exception
        :return str: absolute file path of the given relative file path
        :raises RuntimeError: if the file path does not exist and
                              quit_on_error is True
        """
        if check_relative_to_path:
            abs_file_path = self._get_abs_file_path_to_this_file(rel_file_path)
        else:
            abs_file_path = self._get_abs_file_path_to_config_file(rel_file_path)

        if not os.path.exists(abs_file_path):
            if quit_on_error:
                raise RuntimeError("File '%s' does not exist." % abs_file_path)
            else:
                self.logger.warning("File '%s' does not exist." % abs_file_path)

        return abs_file_path

    def _get_abs_file_path_to_this_file(self, rel_file_path):
        """
        Returns the absolute file path of the given [relative] file path
        to this file.

        :param user rel_file_path: relative file path
        :return str: absolute file path of the given relative file path
        """
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            rel_file_path)

    def _get_abs_file_path_to_config_file(self, rel_file_path):
        """
        Returns the absolute file path of the given [relative] file path
        to the config file.

        :param user rel_file_path: relative file path
        :return str: absolute file path of the given relative file path
        """
        return os.path.join(
            self._config_file_dir,
            rel_file_path)

