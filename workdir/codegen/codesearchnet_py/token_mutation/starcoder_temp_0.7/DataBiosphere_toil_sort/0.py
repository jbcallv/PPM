def sort(in_file, out_file):
    """Sorts the given file.
    """
    with open(in_file, 'r') as infile:
        lines = infile.readlines()
        lines = sorted(lines)
        with open(out_file, 'w') as outfile:
            outfile.writelines(lines)

