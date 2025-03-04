def read_file(self, path):
        """
        Reads a file into memory and reads it's contents

        @type path: str
        @param path: file to load
        """
        with open(path, 'r') as f:
            data = f.read()
        return data

    def find_file(self, path):
        """
        Finds a file on the file system

        @type path: str
        @param path: path to file
        """
        return os.path.exists(path)

    def find_files(self, path, pattern):
        """
        Finds files on the file system

        @type path: str
        @param path: path to file
        @type pattern: str
        @param pattern: regex pattern
        """
        return glob.glob(path + "/" + pattern)

