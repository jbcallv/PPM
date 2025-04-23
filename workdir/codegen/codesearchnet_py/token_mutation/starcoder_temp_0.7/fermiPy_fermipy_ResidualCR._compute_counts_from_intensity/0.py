def _compute_counts_from_intensity(intensity, bexpcube):
        """ road the " map from the intensity
        """
        return (bexpcube.full_model_counts * intensity)

