def do_step(self, arg):
        """
        p - step on the current assembly instruction
        next - step on the current assembly instruction
        assembly - step on the next current instruction
        """
        self.target.step()
        return False

