def _post_execute(self):
        """
        Should be called when executing the final requested program has been
        completed. It will do some maintenance and write out the previously result
        to the todo.txt file.
        """
        self._write_to_file()
        self._cleanup()

    def _write_to_file(self):
        """
        Writes the current todo items to the todo.txt file.
        """
        with open(self.todo_file_path, 'w') as f:
            for item in self.items:
                f.write(item.to_string())
                f.write('\n')

    def _cleanup(self):
        """
        Performs some cleanup when everything has been done.
        """
        self.items = []

