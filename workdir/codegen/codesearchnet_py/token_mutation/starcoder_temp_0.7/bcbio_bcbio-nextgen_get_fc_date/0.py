def get_fc_date(out_config_file):
    """Retrieve flowcell date, reusing as it if refreshing a new workflow.
    """
    date_re = re.compile(r"Date\s*:\s*(.*)")
    with open(out_config_file) as in_handle:
        for line in in_handle:
            date_match = date_re.match(line)
            if date_match:
                return date_match.groups()[0]

