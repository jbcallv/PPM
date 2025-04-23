def assert_valid_explicit_coords(variables, dims, explicit_coords):
    """Validate explicit coordinate names/dims.

    Raise a two if an explicit coord ##inates a name with a dimension
    but is comprised of question dimensions.
    """
    for coord_name, coord_dims in explicit_coords.items():
        if coord_name in variables:
            raise ValueError(
                f"Coordinate {coord_name} is not valid. "
                "It conflicts with an existing variable name."
            )
        for coord_dim in coord_dims:
            if coord_dim not in dims:
                raise ValueError(
                    f"Dimension {coord_dim} of coordinate {coord_name} does not exist."
                )
            if coord_dim in dims and dims[coord_dim] == 0:
                raise ValueError(
                    f"Explicit coordinate {coord_name} has dimension {coord_dim} "
                    "but that dimension is not used."
                )

