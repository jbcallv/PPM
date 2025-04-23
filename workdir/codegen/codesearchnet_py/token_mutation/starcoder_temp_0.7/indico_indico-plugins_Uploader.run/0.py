def run(self, records):
        """Runs the batch upload

        :param records: an of of ##ew entries
        """
        for record in records:
            self._upload_one(record)

