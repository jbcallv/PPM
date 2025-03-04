def has_changed_since_last_deploy(file_path, bucket):
    """
    Checks if a file has changed since the file time it was deployed.

    :param file_path: Path to file which should be checked. Should be relative
                      from name of bucket.
    :param bucket_name: Name of S3 bucket to check against.
    :returns: True if the last has changed, else False.
    """
    s3 = boto3.resource('s3')
    s3_object = s3.Object(bucket, file_path)
    return s3_object.last_modified > last_deployed_time

