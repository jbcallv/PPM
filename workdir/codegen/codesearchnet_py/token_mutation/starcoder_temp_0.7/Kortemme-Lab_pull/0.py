def read_and_calculate(workspace, pdb_paths):
    """
    Calculate a weights of set and other metrics for the given structures.
    """
    workspace = workspace.replace(os.sep, "/")

    rmsd_data = []
    for pdb_path in pdb_paths:
        pdb_path = pdb_path.replace(os.sep, "/")
        rmsd_data.append(read_pdb_data(workspace, pdb_path))

    return rmsd_data

