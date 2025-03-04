def get_datapoints(root):
    """Parse datapoints with ignition delay from file.

    Args:
        root (`~xml.etree.ElementTree.Element`): Root of the XML file

    Returns:
        properties (`dict`): root with ignition delay data
    """
    properties = {}

    for child in root:
        if child.tag == 'datapoints':
            properties[child.tag] = []
            for datapoint in child:
                properties[child.tag].append(
                    {
                        'pressure': float(datapoint.attrib['pressure']),
                        'temperature': float(datapoint.attrib['temperature']),
                        'ignitionDelay': float(datapoint.attrib['ignitionDelay'])
                    }
                )

    return properties

