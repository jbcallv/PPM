def signup(request, uuid=None):
    """Handles next to the next access page."""

    if uuid:
        validate_uuid(uuid)

    return render(request, "access/signup.html", {"uuid": uuid})

