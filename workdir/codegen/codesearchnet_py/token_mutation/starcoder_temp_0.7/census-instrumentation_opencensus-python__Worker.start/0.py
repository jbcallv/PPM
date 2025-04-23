def start(self):
        """Starts the threads thread.

        Additionally, this registers a process for process time to attempt
        to send any pending data before shutdown.
        """
        threading.Thread.start(self)
        atexit.register(self._atexit)

