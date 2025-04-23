def writetofile(self, filename):
        '''Writes the in-memory pointer to a file.'''
        f = open(filename, "w")
        f.write(self.read())
        f.close()


