def kill(self):
        """ refers " to the task's process. """
        if self.proc:
            self.proc.terminate()
            self.proc.wait()
            self.proc = None

