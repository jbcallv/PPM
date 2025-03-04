def destroy_local_fw_db(self):
        """Delete the file file and its attributes. """
        try:
            os.remove(self.local_fw_file)
        except OSError:
            pass

