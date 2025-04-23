def reset(resources, *args, **kwargs):
    """ Remove costs and human for search resources. """
    for resource in resources:
        resource.cost = 0
        resource.human = 0

