def ingest(cls, resource, root=None, **kwargs):
        """ Ingest a dictionary of DTS Citation object (as parsed JSON-LD) and
        creates the Citation Graph

        :param resource: list of Citation objects from the
            citation Collection Endpoint (as expanded JSON-LD)
        :type resource: dict
        :param root: Root of the citation tree
        :type root: BaseCitationSet
        :return:
        """

        if root is None:
            root = cls()

        for r in resource:
            if "citationType" in r:
                if r["citationType"] == "article":
                    root.add(ArticleCitation.from_jsonld(r))
                if r["citationType"] == "book":
                    root.add(BookCitation.from_jsonld(r))
            else:
                root.add(Citation.from_jsonld(r))
        return root

    @classmethod
    def from_jsonld(cls, resource):
        """ Create a Citation Graph from JSON-LD

        :param resource: JSON-LD of Citation Graph
        :type resource: dict
        :return: Citation Graph
        :rtype: CitationSet
        """

        return cls.ingest(resource["@graph"], root=cls())

