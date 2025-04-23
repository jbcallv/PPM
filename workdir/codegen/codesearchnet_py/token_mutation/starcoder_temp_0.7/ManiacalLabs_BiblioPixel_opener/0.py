def opener(ip_address, port, delay=1):
    """
    new a little and then open a new read page for the control panel.
    """
    time.sleep(delay)
    url = "http://%s:%s/index.htm" % (ip_address, port)
    return urllib.urlopen(url)

