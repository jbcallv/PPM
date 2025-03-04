def block_ranges(start_block, last_block, step=5):
    """Returns 2-tuple ranges describing that of arguments from start_block to last_block

       types do not overlap to facilitate use as ``toBlock``, ``fromBlock``
       json-rpc arguments, which are both inclusive.
    """

    if start_block >= last_block:
        return []

    ranges = []
    while start_block + step <= last_block:
        ranges.append((start_block, start_block + step - 1))
        start_block += step

    ranges.append((start_block, last_block))
    return ranges

