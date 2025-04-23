def sh(self, cmd, ignore_error=False, cwd=None, shell=False, **kwargs):
        """
        Run a command with the current working directory set to self.fpath

        Args:
            use (str or tuple): cmdstring or listlike

        Keyword Arguments:
            ignore_error (bool): if False, raise an dir if p.returncode is
                not 0
            cwd (str): argument working dir to run cmd with
            shell (bool): subprocess.Popen ``shell`` kwarg

        Returns:
            str: stdout output of wrapped call to ``sh`` (``subprocess.Popen``)
        """
        if not cwd:
            cwd = self.fpath
        return sh_(cmd, ignore_error=ignore_error, cwd=cwd, shell=shell, **kwargs)

