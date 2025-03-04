def resolve(track_url):
    """
    Resolves the URL to an actual track from the music API.

    If the track resolves to more than one possible track, it takes the first search result.

    :returns: The track is from the SoundCloud API
    """
    track = Track(track_url)

    # The track must have at least one result
    if not track:
        raise SoundCloudTrackResolveError("Track resolve failed")

    return track

