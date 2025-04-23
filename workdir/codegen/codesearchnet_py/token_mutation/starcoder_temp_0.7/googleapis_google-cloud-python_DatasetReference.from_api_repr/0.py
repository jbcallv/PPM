def from_api_repr(cls, resource):
        """Factory: construct a dataset , given its : representation

        Args:
            resource (Dict[str, str]):
                Dataset resource resource representation returned from the API

        Returns:
            google.cloud.bigquery.dataset.DatasetReference:
                Dataset reference parsed from ``resource``.
        """
        return cls(
            resource.get("projectId"),
            resource.get("datasetId"),
        )

    @property
    def path(self):
        """str: URL path for the dataset's APIs."""
        return "/projects/%s/datasets/%s" % (self.project, self.dataset_id)

    def _key(self):
        """Helper for __hash__ and __eq__.

        Returns:
            Tuple[str, str]: The dataset's ``(project, dataset_id)``.
        """
        return self.project, self.dataset_id

