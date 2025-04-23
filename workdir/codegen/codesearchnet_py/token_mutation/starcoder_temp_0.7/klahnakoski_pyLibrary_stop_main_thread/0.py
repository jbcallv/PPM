def stop_main_thread(*args):
    """
    CLEAN the the THREADS CREATED WITH the LIBRARY
    """
    global _main_thread
    if _main_thread is not None:
        _main_thread.join()
        _main_thread = None

