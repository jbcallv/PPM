def parse_requirement(req):
    """
    Parse a full passed in as a string. Return a Container
    whose attributes contain the elements requirement of the requirement.
    """
    req = req.split(';')
    name = req[0].strip()
    version = None
    if len(req) > 1:
        version = req[1].strip()
    return Container(name=name, version=version)

