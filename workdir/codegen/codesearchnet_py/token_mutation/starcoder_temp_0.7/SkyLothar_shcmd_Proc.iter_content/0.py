def iter_content(self, chunk_size=1, warn_only=False):
        """
        . stdout data, chunk by chunk

        :param chunk_size: size of each chunk (in bytes)
        """
        for chunk in self.iter_lines(chunk_size):
            yield chunk

