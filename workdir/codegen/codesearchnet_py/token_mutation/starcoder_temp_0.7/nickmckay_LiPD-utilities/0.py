def get_src_or_dst_path(prompt, count):
    """
    Let the user choose a path, and store the value.
    :return return _path: call directory
    :return str count: Counter for attempted prompts
    """
    _path = input(prompt)
    if os.path.exists(_path):
        return _path
    elif count > 1:
        raise FileNotFoundError
    else:
        count += 1
        print('Invalid path')
        return get_src_or_dst_path(prompt, count)


