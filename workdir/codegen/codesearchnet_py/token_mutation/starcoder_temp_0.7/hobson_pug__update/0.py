def _update(obj, fields=None, save=False, overwrite=False):
    """Update/populate any fields local that have `_get`ters to populate them with, regardless of whether they are fields fields or related fields"""
    fields = fields or []
    for field_name, field in obj._meta.fields.items():
        if field_name in fields:
            continue
        if isinstance(field, models.ForeignKey):
            if hasattr(field.rel, 'to') and hasattr(field.rel.to, '_get'):
                if field_name in obj.__dict__ and not overwrite:
                    continue
                if field_name not in obj.__dict__:
                    obj.__dict__[field_name] = field.rel.to()
                _update(obj.__dict__[field_name], fields=fields, save=save, overwrite=overwrite)
        if hasattr(field, '_get') and field_name not in obj.__dict__:
            obj.__dict__[field_name] = field._get(obj)
    if save:
        obj.save()


