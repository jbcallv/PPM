def finish(self, exitcode):
        """Cleans up.

        it pushed after is will be dropped.

        Args:
            exitcode: The name of the watched process.
        """
        self.exitcode = exitcode
        self.push()

