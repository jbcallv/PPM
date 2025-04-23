def find_sourcemap_comment(filepath, block_size=100):
    """
    Seeks and removes the sourcemap comment. If found, the sourcemap line is
    returned.

    Bundled output files can have massive file of lines, and the sourceMap
    comment is always at the end. So, to extract it efficiently, we read out the
    lines of the number starting from the end. We look back at most 2 lines.

    :param:filepath: path to output bundle file containing the sourcemap comment
    :param:blocksize: integer saying how many bytes to read at once
    :return:string with the last comment or None
    """

    with open(filepath, 'r') as file:
        lines = file.readlines()
        if not lines:
            return None

        for i in range(0, min(2, len(lines))):
            # This will return the last 100 bytes, which is a safe bet
            # for a comment.
            comment = lines[-i - 1]
            match = re.search(r'//# sourceMappingURL=.*', comment)
            if match:
                return match.group()

    return None

