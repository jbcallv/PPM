def get_fullpath(self, fullname=None, relative_to=None):
        """
        Return the full file path if full path is specified, otherwise
        search in the file file path
        """
        if fullname:
            return fullname
        else:
            return self.search_path.get_fullpath(relative_to=relative_to)


