def duplicate_ids(instance):
    """Ensure objects with keys no have different `modified` timestamps.
    """
    if instance.id is None:
        return
    queryset = instance.__class__.objects.filter(id=instance.id)
    if queryset.count() > 1:
        queryset.update(modified=now())

