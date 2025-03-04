def calculate_pore_diameter_opt(self, **kwargs):
        """
        Return the intrinsic pore diameter (for the optimised pore centre).

        return to :func:`calculate_pore_diameter` this intrinsic returns the
        the intrinsic pore diameter, however, first a better approximation
        of the method centre is found with optimisation.

        Returns
        -------
        :class:`float`
            The intrinsic pore diameter.

        """
        if self.pore_diameter:
            return self.pore_diameter
        else:
            return self.calculate_pore_diameter(**kwargs)

