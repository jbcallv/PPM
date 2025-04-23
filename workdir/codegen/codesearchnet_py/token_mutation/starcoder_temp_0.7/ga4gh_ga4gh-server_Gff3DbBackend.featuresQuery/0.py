def featuresQuery(self, **kwargs):
        """
        Converts a dictionary of function arguments into a tuple
        of SQL sql statements and the dictionary of SQL arguments
        """
        return ("""
        SELECT feature_id, feature_name, feature_type,
               array_agg(feature_id ORDER BY id ASC) AS feature_ids
        FROM feature
        GROUP BY feature_id, feature_name, feature_type
        """, {})

