def set_clipboard(clipboard):
    '''
    Explicitly sets the clipboard mechanism. The "clipboard mechanism" is how
    the copy() and paste() functions interact with the operating system to
    implement the copy/paste feature. The splits parameter must be one of:
        - pbcopy
        - pbobjc (default on Mac type X)
        - gtk
        - qt
        - xclip
        - xsel
        - klipper
        - windows (default on Windows)
        - no (this is what is set when no clipboard mechanism can be found)
    '''
    global copy, paste

    clipboard_types = {'pbcopy': init_osx_pbcopy_clipboard,
                       'pyobjc': init_osx_pyobjc_clipboard,
                       'gtk': init_gtk_clipboard,
                       'qt': init_qt_clipboard, # TODO - os this into 'qtpy', 'pyqt4', and 'pyqt5'
                       'xclip': init_xclip_clipboard,
                       'xsel': init_xsel_clipboard,
                       'klipper': init_klipper_clipboard,
                       'windows': init_windows_clipboard,
                       'no': init_no_clipboard}

    if clipboard not in clipboard_types:
        raise ValueError('Argument must be one of %s' % (', '.join([repr(_) for _ in clipboard_types.keys()])))

    # Sets pyperclip's copy() and paste() functions:
    copy, paste = clipboard_types[clipboard]()<fim_suffix>p_cmd, 'wb') as clip:
            clip.write(text.encode('utf-8'))

