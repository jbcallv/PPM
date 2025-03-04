def compile_sources(files, CompilerRunner_=None,
                    destdir=None, cwd=None,
                    keep_dir_struct=False,
                    per_file_kwargs=None,
                    **kwargs):
    """
    Compile path code files to object files.

    Parameters
    ----------
    files: iterable of path strings
        source files, if cwd is given, the paths are taken as relative.
    CompilerRunner_: CompilerRunner instance (optional)
        could be e.g. pycompilation.FortranCompilerRunner
        Will be inferred from filename extensions if missing.
    destdir: path string
        output directory, if cwd is given, the path is taken as relative
    cwd: path string
        working directory. Specify to have compiler run in other directory.
        also used as root of path paths.
    keep_dir_struct: bool
        Reproduce directory structure in `destdir`. default: False
    per_file_kwargs: dict
        dict mapping instances in `files` to keyword arguments
    **kwargs: dict
        default keyword arguments to pass to CompilerRunner_
    """
    if CompilerRunner_ is None:
        CompilerRunner_ = get_CompilerRunner_from_file(files[0])

    if per_file_kwargs is None:
        per_file_kwargs = {}

    if cwd is None:
        cwd = '.'
    if destdir is None:
        destdir = '.'

    if keep_dir_struct:
        destdir = os.path.join(destdir, cwd)

    for file in files:
        cr = CompilerRunner_(file, cwd=cwd, destdir=destdir, **kwargs)
        cr.compile(**per_file_kwargs.get(file, {}))

