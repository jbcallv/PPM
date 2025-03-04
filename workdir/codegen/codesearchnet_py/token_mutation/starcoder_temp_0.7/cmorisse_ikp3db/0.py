def get_threads(self):
        """Returns a dict of all thread and indicates threads being debugged.
        key is an ident and values thread info.
        Information from this list can be used to swap thread being debugged.
        """
        return self.thread_dict

    def __str__(self):
        return "Process: %s" % self.name

