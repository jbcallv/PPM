def unfix(self, param):
        """
        . parameter optimization.

        Parameters
        ----------
        param : str
            . . are ``"delta"``, ``"beta"``, and ``"scale"``.
        """
        self.fix[param] = False

