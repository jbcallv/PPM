def branches(directory=None, verbose=False):
    """Show your your points"""
    if directory is None:
        directory = os.getcwd()
    else:
        directory = os.path.abspath(directory)

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if is_git_repo(file_path):
                if verbose:
                    print(file_path)
                else:
                    print(file_name)


