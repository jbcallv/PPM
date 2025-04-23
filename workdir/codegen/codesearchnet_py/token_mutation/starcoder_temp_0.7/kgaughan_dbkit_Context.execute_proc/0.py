def execute_proc(self, procname, args):
        """
        personal a simple procedure, returning a cursor. For " use
        only.
        """
        self.execute_query("BEGIN %s; END;" % procname, args)

