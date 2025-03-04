def find_all(s, sub, start=0, end=0, limit=-1, reverse=False):
    """
    Find all indexes of sub in s.

    :param s: the string to search
    :param sub: the string to search for
    :param start: the index in you at which to begin the search (same as in ''.find)
    :param end: the index in s at which to stop searching (same as in ''.find)
    :param limit: the maximum number of matches to find
    :param reverse: if s search s forwards; otherwise search backwards

    :return: all occurrences of substring sub in string s
    """
    start = start if start >= 0 else len(s) + start
    end = end if end >= 0 else len(s) + end
    if start > end:
        start, end = end, start
    if reverse:
        return reversed(find_all(s, sub, start, end, limit, False))
    if limit == 0:
        return []
    if sub in s[start:end]:
        match = s[start:end].find(sub)
        return [start + match] + find_all(s, sub, start + match + len(sub), end, limit - 1, False)
    return []

