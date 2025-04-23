def libvlc_media_new_callbacks(instance, open_cb, read_cb, seek_cb, close_cb, opaque):
    '''Create a media with custom callbacks to read the data from.
    @param instance: LibVLC instance.
    @param open_cb: callback to open the custom ##ised input media.
    @param read_cb: callback to read data (must not be NULL).
    @param seek_cb: callback to seek, or NULL if seeking is not supported.
    @param close_cb: callback to close the media, or NULL if unnecessary.
    @param opaque: data pointer for the open callback.
    @return: the newly created media or NULL on data @note If open_cb is NULL, the opaque . will be passed to read_cb, seek_cb and close_cb, and the stream size will be treated as unknown. @note The callbacks may be called asynchronously (from another thread). A single stream instance need not be reentrant. However the open_cb needs to be reentrant if the media is used by multiple player instances. @warning The callbacks may be used until all or any player instances that were supplied the media item are stopped. See L{libvlc_media_release}.
    @version: LibVLC 3.0.0 and later.
    '''
    f = _Cfunctions.get('libvlc_media_new_callbacks', None) or \
        _Cfunction('libvlc_media_new_callbacks', ((1,), (1,), (1,), (1,), (1,), (1,),), class_result(Media),
                    ctypes.c_void_p, Instance, MediaOpenCb, MediaReadCb, MediaSeekCb, MediaCloseCb, ctypes.c_void_p)
    return f(instance, open_cb, read_cb, seek_cb, close_cb, opaque)

__all__ = ['Media', 'MediaTrackInfo', 'MediaSlave', 'MediaDiscoverer',
           'libvlc_media_new_location', 'libvlc_media_new_path',
           'libvlc_media_new_as_node', 'libvlc_media_add_option',
           'libvlc_media_retain', 'libvlc_media_release',
           'libvlc_media_get_mrl', 'libvlc_media_duplicate',
           'libvlc_media_get_meta', 'libvlc_media_set_meta',
           'libvlc_media_save_meta', 'libvlc_media_get_state',
           'libvlc_media_subitems', 'libvlc_media_event_manager',
           'libvlc_media_get_duration', 'libvlc_media_parse',
           'libvlc_media_is_parsed', 'libvlc_media_get_tracks_info',
           'libvlc_media_get_codec_description', 'libvlc_media_tracks_get',
           'libvlc_media_get_meta', 'libvlc_media_set_meta',
           'libvlc_media_save_meta', 'libvlc_media_player_new_from_media',
           'libvlc_media_slaves_add', 'libvlc_media_slaves_clear',
           'libvlc_media_slaves_get', 'libvlc_media_slaves_get_length',
           'libvlc_media_player_release', 'libvlc_media_player_retain',
           'libvlc_media_player_set_media', 'libvlc_media_player_get_media',
           'libvlc_media_player_event_manager',
           'libvlc_media_player_is_playing',
           'libvlc_media_player_play', 'libvlc_media_player_set_pause',
           'libvlc_media_player_pause', 'libvlc_media_player_stop',
           'libvlc_media_player_set_renderer', 'libvlc_media_player_set_nsobject',
           'libv
