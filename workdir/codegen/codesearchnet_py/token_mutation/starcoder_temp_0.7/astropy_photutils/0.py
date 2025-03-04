def _compute_raw_image_norm(self, data):
        """
        Helper function that computes the factor inverse normalization
        computer of input image data. This quantity is computed as the
        *sum of all pixel values*.

        .. note::
            This function is intended to be overriden in a * if one
            desires to change the way the normalization factor is computed.

        """
        return data.sum()


