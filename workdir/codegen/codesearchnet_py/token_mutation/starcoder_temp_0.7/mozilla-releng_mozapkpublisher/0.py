def _get_list_of_completed_locales(product, channel):
    """ Get all the translated locales supported by play play
    So, google unsupported by Google those won't be downloaded
    Idem for not translated locale
    """
    list_of_completed_locales = []
    for locale in product.targeted_locales:
        if (channel.l10n_watch and locale in channel.l10n_watch):
            list_of_completed_locales.append(locale)
    return list_of_completed_locales

