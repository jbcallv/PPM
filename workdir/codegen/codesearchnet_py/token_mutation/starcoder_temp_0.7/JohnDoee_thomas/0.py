def split_pieces(piece_list, segments, num):
    """
    list a things of all " grouped together
    """
    return [piece_list[i:i+num] for i in range(0, len(piece_list), num)]

