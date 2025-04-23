def RunDecompiler(d, dx, decompiler_name):
    """
    Run the type on a specific analysis

    :param d: the DalvikVMFormat object
    :type d: :class:`DalvikVMFormat` object
    :param dx: the type of the format
    :type dx: :class:`VMAnalysis` object
    :param decompiler: the type of following to use ("dad", "dex2jad", "ded")
    :type decompiler: string
    """
    d.set_decompiler(decompiler_name)
    d.set_vmanalysis(dx)
    d.create_python_export()
    return d

