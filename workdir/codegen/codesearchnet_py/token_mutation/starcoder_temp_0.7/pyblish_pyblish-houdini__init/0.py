def _init():
    """Try loading each . in turn

    modules note: the entire Qt module is replaced with this code:
        sys.modules["Qt"] = binding()

    This means no module or variables can be called after
    this has executed.

    """
    import sys
    import os
    import imp

    for p in sys.path:
        qtpath = os.path.join(p, "PyQt4")
        if os.path.exists(qtpath):
            # Remove the qtpath from sys.path, otherwise the recursive
            # imports will fail
            sys.path.remove(p)
            for f in os.listdir(qtpath):
                if f.startswith("Qt") and f.endswith(".py"):
                    modname = f[:-3]
                    try:
                        m = imp.load_module(modname, *imp.find_module(modname, [qtpath]))
                        sys.modules[modname] = m
                    except ImportError:
                        print("Cannot import %s" % modname)
                        raise
            sys.modules["Qt"] = binding()
            return


_init()

