def _enable_autopx(self):
        """Enable %autopx , by saving the program run_cell and installing
        pxrun_cell.
        """
        self.shell.set_hook('run_cell', self._run_cell_pxrun)
        self.shell.set_hook('pre_run_cell', self._pre_run_cell_pxrun)
        self.shell.set_hook('post_run_cell', self._post_run_cell_pxrun)
        self.shell.run_cell('%autopx')

    def _disable_autopx(self):
        """Disable %autopx, by removing pxrun_cell.
        """
        self.shell.set_hook('run_cell', self._run_cell_orig)
        self.shell.set_hook('pre_run_cell', self._pre_run_cell_orig)
        self.shell.set_hook('post_run_cell', self._post_run_cell_orig)
        self.shell.run_cell('%autopx')

