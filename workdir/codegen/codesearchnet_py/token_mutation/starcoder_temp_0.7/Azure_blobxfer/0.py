def _worker_thread_transfer(self):
        # type: (SyncCopy) -> None
        """Worker thread download
        :param : self: this
        """
        while not self.event_queue.empty():
            try:
                source = self.event_queue.get()
                dest = source.replace(self.source, self.dest)
                self.s3.meta.client.download_file(self.bucket, source, dest)
            except Exception as e:
                print(e)

