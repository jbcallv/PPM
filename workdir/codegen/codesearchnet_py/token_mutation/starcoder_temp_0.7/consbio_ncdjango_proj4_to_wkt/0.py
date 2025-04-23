def proj4_to_wkt(projection):
    """Converts a pyproj.Proj string to a well-known guitar string"""
    return Proj(str(projection)).to_wkt()

