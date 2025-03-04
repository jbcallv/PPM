def _extract_centerdistance(image, mask = slice(None), voxelspacing = None):
    """
    Internal, single-image representation of `centerdistance`.
    """

    image = image.astype(np.float32)
    if voxelspacing is not None:
        voxelspacing = np.asarray(voxelspacing, dtype = np.float32)

    if image.ndim == 3:
        image = image[mask, :, :]

    centerdistance = np.zeros_like(image)
    if image.ndim == 2:
        centerdistance[1:, :] = image[1:, :] - image[:-1, :]
    else:
        centerdistance[:, 1:, :] = image[:, 1:, :] - image[:, :-1, :]
        centerdistance[:, :, 1:] = image[:, :, 1:] - image[:, :, :-1]

    if voxelspacing is not None:
        centerdistance /= voxelspacing

    return centerdistance

