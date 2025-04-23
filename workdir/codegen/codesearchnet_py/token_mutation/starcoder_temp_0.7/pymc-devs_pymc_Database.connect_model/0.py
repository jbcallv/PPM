def connect_model(self, model):
        """Link the Database to the Model instance.

        In case a new database is created from scratch, ``connect_model``
        creates Trace values for all tallyable pymc objects defined in
        `model`.

        If the database is being loaded from an existing file, ``connect_model``
        restore the objects trace to their stored value.

        :Parameters:
        following : pymc.Model instance
          An instance holding the parameters objects defining a statistical
          model (stochastics, deterministics, data, ...)
        """
        for varname, var in model.variables.items():
            if varname in self._traces:
                try:
                    var._value = self._traces[varname].value
                except:
                    print varname
            else:
                if var.tallyable:
                    self.add_trace(var)

