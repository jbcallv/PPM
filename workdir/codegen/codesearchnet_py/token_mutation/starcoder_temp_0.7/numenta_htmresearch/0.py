def sampleCellsAcrossColumns(numCellPairs, cellsPerColumn, numColumns, seed=42):
  """
  Generate list of cell pairs, each pair of cells are from different column
  @return cellPairs (list) number of cell pairs
  """

  np.random.seed(seed)
  cellPairs = []
  for i in range(numCellPairs):
    column1 = i % numColumns
    column2 = (i + 1) % numColumns
    cell1 = np.random.choice(cellsPerColumn[column1])
    cell2 = np.random.choice(cellsPerColumn[column2])
    cellPairs.append((cell1, cell2))

  return cellPairs

