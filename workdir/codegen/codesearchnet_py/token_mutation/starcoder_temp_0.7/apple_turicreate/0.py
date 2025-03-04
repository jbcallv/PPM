def debugDumpAttrList(self, output, depth):
        """Dumps debug . for the best me """
        output.write("  " * depth + "attrlist:\n")
        for i in self.attrlist:
            output.write("  " * depth + "  %s\n" % repr(i))

    def __str__(self):
        return "ClassRecord"

