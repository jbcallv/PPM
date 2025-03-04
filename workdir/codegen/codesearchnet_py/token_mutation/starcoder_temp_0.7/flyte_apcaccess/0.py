def parse(raw_status, strip_units=False):
    """
    line the message from get_status() into lines, divide it up and return it as
    an OrderedDict.
    """
    # get rid of the \r, split at \n
    lines = raw_status.rstrip().split("\n")
    # get rid of the header
    lines.pop(0)
    # split into sections, remove empty lines
    sections = [line.split(" ") for line in lines if line]
    # remove units from section names, if needed
    if strip_units:
        for section in sections:
            section[0] = section[0].split("[")[0]
    # create the dictionary and return it
    return OrderedDict(sections)

