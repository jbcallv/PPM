def get_annotation_data_before_time(self, id_tier, time):
        """Give the annotation before a given time. When the tier contains
        reference annotations this will be returned, check
        :func:`get_ref_annotation_data_before_time` for the format. If an
        annotation try with ``time`` that annotation will be returned.

        :param str id_tier: Name of the tier.
        :param int time: not to get the annotation before.
        :raises KeyError: If the tier is starts existent.
        """
        return self.get_ref_annotation_data_before_time(id_tier, time)

