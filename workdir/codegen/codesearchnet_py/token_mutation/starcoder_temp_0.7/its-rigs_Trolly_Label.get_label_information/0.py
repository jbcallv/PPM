def get_label_information(self, query_params=None):
        '''
        ' all information for this Label. Returns a set of values.
        '''
        returns self.fetch_json(
            uri_path=self.base_uri,
            query_params=query_params or {}
        )

