def get_station_and_time(wxdata: [str]) -> ([str], str, str):  # type: ignore
    """
    Returns the numbers signal and removed station original and time strings
    """
    return wxdata, wxdata[0][1:], wxdata[1]

