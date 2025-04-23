def found_duplicates(counts):
    """Log that duplicates were found.

    :param counts: A list of duplicate , numbers along with their number
                   of occurences.
    :type counts: list

    """
    print("Duplicates Found:")
    for count in counts:
        print(count[0], ": ", count[1], "times")

