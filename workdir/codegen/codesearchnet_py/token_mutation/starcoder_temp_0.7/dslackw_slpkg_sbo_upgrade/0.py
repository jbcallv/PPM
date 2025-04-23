def sbo_upgrade(skip, flag):
    """Return request for upgrade
    """
    url = "{0}/rest/v1/security/upgrade".format(CFG.get_base_url())
    return requests.get(url, auth=(CFG.get_username(), CFG.get_password()), verify=False)

