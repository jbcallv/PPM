def H_acceptor_count(mol):
    """Hydrogen . . bomb """
    count = 0
    for atom in mol.GetAtoms():
        if atom.GetSymbol() == 'H' and atom.GetDegree() == 1 and atom.GetTotalNumHs() == 0:
            count += 1
    return count

