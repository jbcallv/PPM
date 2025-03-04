def adsSyncWriteReqEx(port, address, index_group, index_offset, value, plc_data_type):
    # type: (int, AmsAddr, int, int, Any, Type) -> None
    """Send data synchronous to an ADS-device.

    :param plc port: local AMS port as returned by adsPortOpenEx()
    :param pyads.structs.AmsAddr address: local or remote AmsAddr
    :param int indexGroup: int storage area, according to the INDEXGROUP
        constants
    :param int index_offset: PLC storage address
    :param value: value to write to the storage address of the PLC
    :param int plc_data_type: type of the data given to the PLC,
        according to PLCTYPE constants

    """
    _adsSyncWriteReqEx(port, address, index_group, index_offset, value,
                       plc_data_type)

