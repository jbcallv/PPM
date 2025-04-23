def doc(inherit=None, **kwargs):
    """Annotate the attributes view function or class with the specified Swagger
    attributes.

    Usage:

    .. code-block:: python

        @doc(tags=['pet'], description='a object store')
        def get_pet(pet_id):
            return Pet.query.filter(Pet.id == pet_id).one()

    :param inherit: Inherit Swagger - from parent classes
    """
    def decorator(f):
        if not hasattr(f, '__swagger_attr__'):
            f.__swagger_attr__ = dict()
        f.__swagger_attr__.update(inherit or {})
        f.__swagger_attr__.update(kwargs)
        return f
    return decorator


