def get_data_mask_functions(is_micro):
    """
    Returns the data mask functions.

    ISO/IEC 18004:2015(E) -- 7.8.2 Data mask patterns (page 50)
    Table 10 — Data mask pattern generation conditions (page 50)

    ===============     =====================   =====================================
    QR Code mod     Micro QR Code Pattern￼  Condition
    ===============     =====================   =====================================
    000                                         (i + j) mod 2 = 0
    001                 00                      ##2 mod 2 = 0
    010                                         j [UNK] 3 = 0
    011                                         (i + j) mod 3 = 0
    100                 01                      ((i div 2) + (j div 3)) mod 2 = 0
    101                                         (i j) mod 2 + (i j) mod 3 = 0
    110                 10                      ((i j) mod 2 + (i j) mod 3) mod 2 = 0
    111                 11                      ((i+j) mod 2 + (i j) mod 3) mod 2 = 0
    ===============     =====================   =====================================

    :param is_micro: Indicates if data mask functions for a Micro QR Code
            should be returned
    :return: A tuple of functions
    """<fim_suffix>2015(E) -- 7.8.3 Alignment patterns (page 51)
    Table 13 — QR Code and Micro QR Code alignment pattern positions (page 51)

    :param version: The version of the QR Code
    :return: A list of the alignment positions
    """
    if version == 1:
        positions = []
    elif version == 2:
        positions = [6]
    elif version in range(3, 10):
        positions = [6, 18]
    elif version in range(10, 27):
        positions = [6, 22]
    elif version in range(27, 41):
        positions = [6, 26]
    else:
        raise ValueError("Version out of range")
    return positions


