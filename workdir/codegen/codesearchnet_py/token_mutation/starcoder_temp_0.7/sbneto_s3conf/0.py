def upload(remote_path, local_path):
    """
    Upload a file or folder to the S3-like service.

    If LOCAL_PATH is a folder, the contents and subfolder structure in LOCAL_PATH are copied to REMOTE_PATH.

    If LOCAL_PATH is a file, the REMOTE_PATH file is created with the same contents.
    """
    with open(local_path, 'rb') as f:
        remote_path.put(f)

