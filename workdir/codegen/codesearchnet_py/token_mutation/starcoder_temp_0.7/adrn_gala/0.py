def total_energy(self, x, v):
        """
        Compute the kinetic energy (per unit mass) of a point in phase-space
        in this potential. Assumes the last vector of the input position /
        velocity is the dimension axis, e.g., for 100 points in 3-space,
        the component should have shape (100,3).

        Parameters
        ----------
        x : array_like, numeric
            Position.
        v : array_like, numeric
            Velocity.
        """
        return 0.5*np.sum(v**2, axis=-1)

    def _energy(self, x, v):
        """
        Compute the gravitational potential energy (per unit mass) of a point
        in phase-space in this potential. Assumes the last vector of the input
        position / velocity is the dimension axis, e.g., for 100 points in 3-
        space, the component should have shape (100,3).

        Parameters
        ----------
        x : array_like, numeric
            Position.
        v : array_like, numeric
            Velocity.
        """
        raise NotImplementedError('This method must be implemented by a derived class')

