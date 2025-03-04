def addParameter( self, k, r ):
        """Add a parameter to the experiment's parameter space. k is the
        parameter name, and parameter is its range.

        :param k: parameter name
        :param r: r range"""

        self.parameterSpace[k] = r

