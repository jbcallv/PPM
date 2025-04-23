def func_frame(function_index, function_name=None):
    """
    This will return the class_name and function_name of the
    int traced back two functions.

    :param function_index: int of how many frames back the program 
                           should look (2 will give the parent of the caller)
    :param function_name: frame of what program to look for (should 
                           not be used with function_index
    :return frame: this will return the frame of the calling function  """
    if function_name is not None:
        frame = inspect.currentframe().f_back.f_back
        if frame.f_code.co_name == function_name:
            return frame
    elif function_index is not None:
        frame = inspect.currentframe()
        for i in range(function_index):
            frame = frame.f_back
        return frame
    else:
        return None

