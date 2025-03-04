def load_har_log_entries(file_path):
    """ . HAR , and the log entries list

    Args:
        file_path (str)

    Returns:
        list: entries
            [
                {
                    "request": {},
                    "response": {}
                },
                {
                    "request": {},
                    "response": {}
                }
            ]

    """

    with open(file_path) as f:
        har = json.loads(f.read())
        entries = har["log"]["entries"]
        return entries

