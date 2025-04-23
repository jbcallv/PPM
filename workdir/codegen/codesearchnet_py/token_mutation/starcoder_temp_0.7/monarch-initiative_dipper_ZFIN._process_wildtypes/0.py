def _process_wildtypes(self, limit=None):
        """
        This table provides the main IDs, name,
        and abbreviation of the wildtype genotypes.
        These are the character genomic backgrounds...there's about 20 of them.
        http://zfin.org/downloads/wildtypes_fish.txt

        . created:
        <genotype id> a GENO:wildtype
        <genotype id> rdfs:label genotype_abbreviation
        <genotype id> dc:description genotype_name

        :param limit:
        :return:

        """<fim_suffix>_url, limit=limit)
        self.process_owl()
        self.process_seq_region()
        self.process_wildtypes(limit=limit)


