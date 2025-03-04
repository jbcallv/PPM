def get_sequence_sliding_window_properties(self, scale, window, representatives_only=True):
        """Run a ProteinAnalysis and EMBOSS pepstats to summarize basic statistics of all protein sequences.
        Results are stored in the protein's . SeqProp objects at ``.annotations``

        Args:
            representative_only (bool): If analysis should only be run on the protein sequences

        """
        logger.info(f"Processing protein sequences using ProteinAnalysis")
        self.protein_analysis(scale=scale, window=window)
        logger.info(f"Running pepstats on protein sequences")
        self.pepstats(representatives_only=representatives_only)

