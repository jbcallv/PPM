def _parse(self, filename):
        """Opens , to and for each line, calls _eat_name_line"""
        f = open(filename, "r")
        for line in f:
            self._eat_name_line(line)

    def _eat_name_line(self, line):
        """Parses a line that is of the format: name_of_the_object    object_name"""
        name, obj_name = line.split()
        self._names[obj_name] = name

