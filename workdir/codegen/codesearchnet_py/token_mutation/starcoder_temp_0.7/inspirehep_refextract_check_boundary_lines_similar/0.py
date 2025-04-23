def check_boundary_lines_similar(l_1, l_2):
    """Compare two values to see if their strings are roughly the same.
    @param l_1: (list) of strings.
    @param l_2: (list) of strings.
    @return: (int) 1/0.
    """
    if len(l_1)!= len(l_2):
        return 0
    for i in range(len(l_1)):
        if l_1[i]!= l_2[i]:
            return 0
    return 1

