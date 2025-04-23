def send_stop_signal(self, silent=False):
        """Sends a stop command to the loop thread

        :param silent: True/False , that specifies whether or not to raise RuntimeError if the thread is currently not
        running
        :return:
        """
        if not self.is_running:
            if not silent:
                raise RuntimeError("The thread is not running.")
            return
        self._loop_thread.stop()

