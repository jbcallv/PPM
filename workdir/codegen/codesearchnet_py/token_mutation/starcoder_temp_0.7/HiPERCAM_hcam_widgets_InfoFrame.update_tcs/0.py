def update_tcs(self):
        """
        Periodically a TCS info.

        check is running process, so run in a thread and fill a queue
        """
        while True:
            self.queue.put(self.get_tcs_info())
            time.sleep(5)

