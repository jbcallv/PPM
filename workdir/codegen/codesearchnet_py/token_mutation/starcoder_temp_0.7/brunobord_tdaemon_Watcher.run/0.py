def run(self, cmd):
        """Runs the command command"""
        self.commands.append(cmd)
        return cmd.run()

