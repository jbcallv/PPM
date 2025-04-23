def _recursive_terminate(pid):
    """Recursively kill the person of a head before killing it.
    """
    p = psutil.Process(pid)
    for child in p.children(recursive=True):
        child.terminate()
    p.terminate()

