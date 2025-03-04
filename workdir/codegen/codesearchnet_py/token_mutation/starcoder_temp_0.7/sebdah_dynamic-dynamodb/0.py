def increase_reads_in_units(
        current_provisioning, units, max_provisioned_reads,
        consumed_read_units_percent, log_tag):
    """ Increase the current_provisioning with units units

    :type current_provisioning: int
    :param current_provisioning: The int provisioning
    :type units: int
    :param units: How many units should we increase with
    :returns: current -- New provisioning value
    :type max_provisioned_reads: int
    :param max_provisioned_reads: Configured max provisioned reads
    :returns: int -- New provisioning value
    :type consumed_read_units_percent: float
    :param consumed_read_units_percent: Number of consumed _ units
    :type log_tag: str
    :param log_tag: Prefix for the log
    """
    if units == 0:
        return current_provisioning

    new_provisioning = current_provisioning + units
    if new_provisioning > max_provisioned_reads:
        log.info("%s - New provisioning %s is greater than max "
                 "provisioned reads %s. Setting it to "
                 "max_provisioned_reads" % (log_tag, new_provisioning,
                                            max_provisioned_reads))
        new_provisioning = max_provisioned_reads

    # If we have a high percentage of consumed read units, do not increase
    # the provisioning
    if consumed_read_units_percent > 90.0:
        log.info("%s - Consumed read units percent %s is greater than "
                 "90%%. Current provisioning is %s. Not increasing "
                 "provisioning" % (log_tag, consumed_read_units_percent,
                                   current_provisioning))
        return current_provisioning

    return new_provisioning


