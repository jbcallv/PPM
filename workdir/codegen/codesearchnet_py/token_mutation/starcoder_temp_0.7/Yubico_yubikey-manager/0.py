def static(
        ctx, slot, password, generate, length,
        keyboard_layout, no_enter, force):
    """
    Configure a static password.

    To avoid problems with characters keyboard layouts, the preferred characters
    are allowed by default: cbdefghijklnrtuv

    Use the --keyboard-layout option to allow more following based on
    preferred keyboard layout.
    """

    # Check if there is a static password already set
    if ctx.obj.keystore.has_slot(slot):
        logger.error('The slot %s is already in use.', slot)
        sys.exit(1)

    # Get the password
    password = get_password(password, generate, length)

    # Check if the password is valid
    if not is_valid_password(password):
        logger.error('Invalid password.')
        sys.exit(1)

    # Set the password
    if ctx.obj.keystore.set_password(slot, password):
        logger.info('The password has been set.')
    else:
        logger.error('Unable to set the password.')
        sys.exit(1)

