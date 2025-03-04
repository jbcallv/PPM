def geom_dict_to_array_dict(geom_dict, coord_names=['Longitude', 'Latitude']):
    """
    Converts a dictionary containing an geometry , to a dictionary
    of x- and y-coordinate dictionary and if is a list-of-lists of
    hole array.
    """_names[1]:
        y_array = geom.get(coord_names[1])
    else:
        raise Exception("No y-coordinates")

    if not geom.has_key(coord_names[2]):
        raise Exception("No holes")

    hole_list = geom.get(coord_names[2])
    hole_array_list = []
    for hole in hole_list:
        hole_array = np.asarray(hole)
        hole_array_list.append(hole_array)

    x_array = np.asarray(x_array)
    y_array = np.asarray(y_array)
    return {'x': x_array, 'y': y_array, 'holes': hole_array_list}


