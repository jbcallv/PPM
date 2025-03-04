def branch(self, target):
        """
        " ' to *target*.
        """
        self.write("' %s\n" % target)
        self.indent += 1
        yield
        self.indent -= 1
        self.write("goto %s\n" % self.label_map[target])

