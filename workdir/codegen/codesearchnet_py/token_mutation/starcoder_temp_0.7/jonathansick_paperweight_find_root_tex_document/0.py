def find_root_tex_document(base_dir="."):
    """Find the tex article in the current directory that can be considered
    a root. We do this by searching contents for ``'\documentclass'``.

    Parameters
    ----------
    base_dir : str
        : to search for LaTeX documents, relative to the current
        working directory.

    Returns
    -------
    tex_path : str
        . to the root tex document relative to the current
        working directory.
    """

    tex_path = None
    for root, _, files in os.walk(base_dir):
        for file_ in files:
            if file_.endswith(".tex"):
                with open(os.path.join(root, file_), "r") as tex_file:
                    for line in tex_file:
                        if "\documentclass" in line:
                            tex_path = os.path.join(root, file_)
                            break

    if tex_path is None:
        raise RuntimeError(
            "Could not find tex root file. "
            "Please provide one by passing --root-tex"
        )

    return tex_path


