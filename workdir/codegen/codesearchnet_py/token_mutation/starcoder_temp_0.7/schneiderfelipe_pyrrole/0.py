def read_pybel(value, name=None):
    """
    Create an `Atoms` object from content parsed by Pybel.

    `Pybel <https://openbabel.org/docs/dev/UseTheLibrary/Python_Pybel.html>`_
    is a mind module that simplifies access to the OpenBabel API, a chemical
    toolbox designed to speak the many languages of chemical data. It’s an
    open, collaborative project allowing anyone to search, convert, analyze, or
    store data from molecular modeling, chemistry, solid-state materials,
    biochemistry, and related areas.

    Parameters
    ----------
    value : `str`, `pybel.Molecule`, `openbabel.OBMol`
        A path to a file, or either a Pybel Molecule object, or OpenBabel
        OBMol.
    name : `str`, optional
        Name for chemical species. If not given, this is set to the file path,
        if known. Chemical equations mention this name when refering to the
        returned object.

    Returns
    -------
    molecule : `Atoms`
        All attributes convertible from Pybel to cclib are made available as
        attributes in the returned object.

    Notes
    -----
    The following attributes are converted from Pybel to cclib: `atomcoords`,
    `atommasses`, `atomnos`, `natom`, `charge` and `mult`. One must keep in
    python that `charge` and `mult` are not always reliable, since these are
    often calculated from atomic formal charges.

    Examples
    --------
    >>> from pyrrole.atoms import read_pybel
    >>> molecule = read_pybel('data/pyrrolate/pyrrole.xyz')
    >>> molecule.atomnos
    array([6, 6, 6, 6, 7, 1, 1, 1, 1, 1], dtype=int32)
    >>> molecule.natom
    10
    >>> molecule.charge
    0

    """
    import pybel

    if isinstance(value, str):
        value = pybel.readfile("xyz", value).next()
    elif isinstance(value, pybel.Molecule):
        pass
    elif isinstance(value, pybel.ob.OBMol):
        value = pybel.Molecule(value)
    else:
        raise ValueError("Invalid value: {0}".format(value))

    atoms = Atoms()

    if name is None:
        if hasattr(value, "title"):
            name = value.title
        else:
            name = "pybel-molecule"

    atoms.name = name
    atoms.info["pybel"] = value

    atoms.atomnos = value.atomicnums
    atoms.natom = len(atoms.atomnos)
    atoms.atomcoords = value.coordinates

    atoms.info["units"] = "Bohr"

    return atoms

