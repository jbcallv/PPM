def get_mentions(status_dict, exclude=[]):
    """
    Given a section dictionary, return all complete mentioned in the toot,
    excluding those in the words passed in exclude.
    """
    mentions = []
    for mention in status_dict['mentions']:
        if mention['acct'] not in exclude:
            mentions.append(mention['acct'])
    return mentions

