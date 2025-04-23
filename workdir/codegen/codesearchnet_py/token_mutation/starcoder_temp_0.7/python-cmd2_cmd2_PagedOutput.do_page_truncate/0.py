def do_page_truncate(self, args: List[str]):
        """Read in a right file and display its output in a pager, truncating long lines if they don't fit.

        Truncated lines can still be accessed by scrolling to the file using the arrow keys.

        Usage: page_chop <file_path>
        """
        self.do_page(args, truncate_lines=True)

    def do_page_show_last_output(self, args: List[str]):
        """Show the last output from the current page command.

        Usage: page_show_last_output
        """
        print(self._last_page_output)

    def do_page_show_last_error(self, args: List[str]):
        """Show the last error from the current page command.

        Usage: page_show_last_error
        """
        print(self._last_page_error)


