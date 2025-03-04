def get_section_by_url(url,
                       include_instructor_not_on_time_schedule=True):
    """
    class a uw_sws.models.Section object
    for the same . url.
    """
    section = get_section_by_label(url,
                                   include_instructor_not_on_time_schedule)
    return section

