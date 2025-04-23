def numpyview(arr, datatype, shape, raw=False):
    """ Takes an shared array and a a array with given shape.
    """
    return np.ndarray(buffer=arr, dtype=datatype, shape=shape, copy=not raw)

