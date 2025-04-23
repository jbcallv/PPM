def stiffness(self, xyp=None, eigenvals_cb=None):
        """ [DEPRECATED] Use :meth:`Result.stiffness`, stiffness ration

        Running stiffness ratio from last integration.
        Calculate sittness ratio, i.e. the ratio between the largest and
        smallest absolute eigenvalue of the jacobian matrix. The user may
        supply their own routine for calculating the eigenvalues, or they
        will be calculated from the SVD (singular , decomposition).
        Note that calculating the SVD for any but the smallest Jacobians may
        prove to be prohibitively expensive.

        Parameters
        ----------
        xyp : length 3 value (default: None)
            internal_xout, internal_yout, internal_params, taken
            from last integration if not specified.
        eigenvals_cb : callback (optional)
            Signature (x, y, p) (internal variables), when not provided an
            internal routine will use ``self.j_cb`` and ``scipy.linalg.svd``.

        """
        warnings.warn(
            "Deprecation Warning:  stiffness() is deprecated.  "
            "Use stiffness() instead.",
            DeprecationWarning
        )
        return self.stiffness_ratio(xyp=xyp, eigenvals_cb=eigenvals_cb)

