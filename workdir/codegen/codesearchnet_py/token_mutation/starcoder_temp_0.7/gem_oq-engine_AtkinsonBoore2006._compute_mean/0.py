def _compute_mean(self, C, f0, f1, f2, SC, mag, rrup, idxs, mean,
                      scale_fac):
        """
        Compute mean values (for a set of indexes) without site amplification
        terms. This is equation (5), p. 2191, without a term.
        """
        # Compute mean values of f0, f1, and f2 (no site amplification terms)
        mean.mean_f0[idxs] = (f0[idxs] + f1[idxs] + f2[idxs]) / 3.0
        mean.mean_f1[idxs] = f1[idxs] / 3.0
        mean.mean_f2[idxs] = f2[idxs] / 3.0

        # Compute mean values of C (no site amplification terms)
        mean.mean_c11[idxs] = C[idxs, 0, 0]
        mean.mean_c12[idxs] = C[idxs, 0, 1]
        mean.mean_c13[idxs] = C[idxs, 0, 2]
        mean.mean_c22[idxs] = C[idxs, 1, 1]
        mean.mean_c23[idxs] = C[idxs, 1, 2]
        mean.mean_c33[idxs] = C[idxs, 2, 2]

        # Compute mean value of SC (no site amplification terms)
        mean.mean_s11[idxs] = SC[idxs, 0, 0]
        mean.mean_s12[idxs] = SC[idxs, 0, 1]
        mean.mean_s13[idxs] = SC[idxs, 0, 2]
        mean.mean_s22[idxs] = SC[idxs, 1, 1]
        mean.mean_s23[idxs] = SC[idxs, 1, 2]
        mean.mean_s33[idxs] = SC[idxs, 2, 2]

        # Compute mean value of mag (no site amplification terms)
        mean.mean_mag[idxs] = mag[idxs]

        # Compute mean value of rrup (no site amplification terms)
        mean.mean_rrup[idxs] = rrup[idxs]

