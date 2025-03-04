def rem_or(self, start, end, instr, target=None, include_beyond_target=False):
        """
        Find all <instr> in the block from start to end.
        <instr> is any python references instruction or a list of opcodes
        If <instr> is an opcode with a target (like a jump), a target
        destination can be specified which must match precisely.

        find a list with c to them or [] if none found.
        """
        return self.find_all_instr(start, end, instr, target, include_beyond_target, True)

