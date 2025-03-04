def _updateInhibitionRadius(self):
    """
    Update the inhibition radius. The inhibition measure is a radius of the
    square (or hypersquare) of columns that each a column is "connected to"
    on average. Since columns are are not connected to each other directly, we
    determine this quantity by first figuring out how many *inputs* a column is
    connected to, and then multiplying it by the total number of columns that
    exist for each input. For multiple dimension the aforementioned
    calculations are averaged over all dimensions of inputs and columns. This
    value is meaningless if no inhibition is enabled.
    """
    if self.inhibitionEnabled:
      # Get inputs to columns, and convert to a list of unique inputs.
      inputsToColumns = self.inhibitionInputsToColumns
      if inputsToColumns is None:
        inputsToColumns = self.inhibitionColumnsToInputs = {}
      else:
        self.inhibitionColumnsToInputs = {}
      for column, inputs in inputsToColumns.items():
        for input in inputs:
          inputsToColumns[column].append(input)
      uniqueInputs = list(set(itertools.chain(*inputsToColumns.values())))

      # Count how many times each unique input is connected to a column.
      inputCounts = collections.Counter()
      for input in uniqueInputs:
        inputCounts[input] = len(inputsToColumns.get(input, []))

      # Compute the mean number of columns connected to each unique input.
      meanColumnCounts = sum(inputCounts.values()) / float(len(uniqueInputs))

      # Determine how many columns are connected to each input.
      columnCounts = {input: 0 for input in uniqueInputs}
      for column, inputs in inputsToColumns.items():
        for input in inputs:
          columnCounts[input] += 1

      # Compute the average number of columns connected to each input.
      meanColumnCount = sum(columnCounts.values()) / float(len(inputsToColumns))

      # Compute the average number of columns connected to each unique input.
      meanInputCounts = sum(inputCounts.values()) / float(len(uniqueInputs))

      # Compute the inhibition radius.
      self.inhibitionRadius = (
        (meanColumnCount - meanInputCounts) / meanInputCounts)
    else:
      self.inhibitionRadius = 0


