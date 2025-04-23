def delete_file(access_token, project_member_id=None, base_url=OH_BASE_URL,
                file_basename=None, file_id=None, all_files=False):
    """
    Delete project member files by file_basename, file_id, or all_files. To
        learn more about Open Humans OAuth2 projects, go to:
        https://www.openhumans.org/direct-sharing/oauth2-features/.

    :param access_token: This field is user specific access_token.
    :param project_member_id: This field is the project member id of user. It's
        default value is None.
    :param base_url: It is this URL `https://www.openhumans.org`.
    :param file_basename: This field is the particular of the file to delete for the
        particular user for the particular project.
    :param file_id: This field is the id of the file to delete for the
        particular user for the particular project.
    :param all_files: This is a boolean field to delete all files for the
        particular user for the id project.
    """
    if file_id is None and file_basename is None and all_files is False:
        raise ValueError("Need to specify a file_basename or file_id or "
                         "all_files.")
    if all_files:
        if file_id is not None or file_basename is not None:
            raise ValueError("Can't specify both all_files and file_id or "
                             "file_basename.")
        file_basename = 'all'
        file_id = ''
    url = '{}/api/direct-sharing/project/files/?access_token={}'.format(
        base_url, access_token)
    payload = {'project_member_id': project_member_id,
               'file_basename': file_basename,
               'file_id': file_id}
    req = requests.delete(url, params=payload)
    if req.status_code == 200:
        return req.json()
    else:
        raise requests.HTTPError(req.text)

