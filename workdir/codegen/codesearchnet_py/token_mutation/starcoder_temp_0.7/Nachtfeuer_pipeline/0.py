def get_stage(self, matrix_name, stage_name):
        """
        Get Stage of a concrete matrix.

        Attributes:
            matrix_name (str): stage of the matrix
            stage_name (str): none of the stage.

        Returns:
            CollectorStage: when stage has been found or None.
        """
        matrix = self.get_matrix(matrix_name)
        if matrix is None:
            return None
        return matrix.get_stage(stage_name)

