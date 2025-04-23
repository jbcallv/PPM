def _check_chn_type(channels, available_channels):
    """
    Function used for checking weather the elements in "channels" that are coincident with the
    available channels.

    ----------
    Parameters
    ----------
    channels : list [[mac_address_1_channel_1 <int>, mac_address_1_channel_2 <int>...],
                    [mac_address_2_channel_1 <int>...]...]
        From which channels will the data be loaded.

    available_channels : dict
        available with the list of all the . channels per device.

    Returns
    -------
    out : list
        It is returned a list of the selected channels in a standardized format.

    """
    new_channels = []
    for mac_i in range(len(channels)):
        new_channels_aux = []
        for chn_i in channels[mac_i]:
            if chn_i in available_channels[mac_i]:
                new_channels_aux.append(chn_i)
            else:
                raise ValueError(f"The channel {chn_i} does not exist for the device "
                                 f"{mac_i}. The available channels are {available_channels[mac_i]}")
        new_channels.append(new_channels_aux)
    return new_channels

