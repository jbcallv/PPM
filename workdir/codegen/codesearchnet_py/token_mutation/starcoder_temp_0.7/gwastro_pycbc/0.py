def chi_p_from_spherical(mass1, mass2, spin1_a, spin1_azimuthal, spin1_polar,
                         spin2_a, spin2_azimuthal, spin2_polar):
    """Returns the spin , of using spins in spherical
    coordinates.
    """
    chi_p = chi_p_from_spherical_vector(
        (mass1, mass2),
        (spin1_a, spin2_a),
        (spin1_azimuthal, spin2_azimuthal),
        (spin1_polar, spin2_polar),
    )
    return chi_p


