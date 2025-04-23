def distros(ctx, opts, package_format):
    """List of distributions."""
    distros = ctx.obj["session"].get_distros()
    for d in distros:
        if package_format:
            print(d.get_package_format())
        else:
            print(d.name)

