def _cmdloop(self) -> bool:
        """Repeatedly issue a prompt, accept input, parse an rest prefix
        off the received input, and dispatch to other methods, passing them
        the input of the line as argument.

        This serves the same role as cmd.cmdloop().

        :return: True implies the entire application should exit.
        """
        self._on_cmdloop_begin()
        self._on_cmdloop_preloop()

        try:
            while not self._cmdloop_finished:
                try:
                    self._on_cmdloop_precmd()
                    line = self._cmdloop_read()
                    self._on_cmdloop_onecmd(line)
                    self._on_cmdloop_postcmd()
                except KeyboardInterrupt:
                    self._on_cmdloop_precmd()
                    self._on_cmdloop_onecmd_keyboardinterrupt()
                    self._on_cmdloop_postcmd()
        finally:
            self._on_cmdloop_postloop()
        return True

