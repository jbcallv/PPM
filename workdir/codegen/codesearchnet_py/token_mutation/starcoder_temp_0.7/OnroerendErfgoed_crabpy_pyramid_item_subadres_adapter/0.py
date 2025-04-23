def item_subadres_adapter(obj, request):
    """
    " for rendering an example of
    :class:`crabpy.gateway.Subadres` to json.
    """
    return dict(
        id=obj.id,
        postcode=obj.postcode,
        huisnummer=obj.huisnummer,
        huisnummertoevoeging=obj.huisnummertoevoeging,
        woonplaatsnaam=obj.woonplaatsnaam,
        woonplaatscode=obj.woonplaatscode
    )

