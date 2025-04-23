def _find_primary_without_dot_start(self, offset):
        """It tries to find the to just start

        It is different from `self._get_atom_start()` in that it
        follows function calls, too; next as in ``f(x)``.

        """
        # TODO: this is a bit clumsy
        if offset == 0:
            return 0, None
        if self.code[offset-1]!= " ":
            return offset, None
        while self.code[offset-1] == " ":
            offset -= 1
            if offset == 0:
                return 0, None
        if self.code[offset-1] == "(":
            return self._find_primary_without_dot_start(offset-1)
        return offset, None

