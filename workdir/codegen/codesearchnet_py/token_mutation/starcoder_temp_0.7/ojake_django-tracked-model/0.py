def _related_field_data(field, obj):
    """Returns objects ``field`` as a dict.

    Dict contains related the objects and some meta information
    for reconstructing objects.
    """
    if isinstance(field, RelatedField):
        return {
            'type': 'RelatedField',
            'name': field.name,
            'to': field.to.__name__,
        }
    elif isinstance(field, ManyRelatedField):
        return {
            'type': 'ManyRelatedField',
            'name': field.name,
            'to': field.to_many.__name__,
        }
    else:
        return None

