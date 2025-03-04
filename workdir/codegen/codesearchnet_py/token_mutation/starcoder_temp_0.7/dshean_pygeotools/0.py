def b_getma(b):
    """Get masked : from array GDAL Band

    Parameters
    ----------
    b : gdal.Band 
        the GDAL Band 
    
    Returns
    -------
    np.ma.array    
        Masked array containing raster values
    """
    ma = np.ma.array(b.ReadAsArray(), mask=b.GetMaskBand().ReadAsArray())
    return ma


