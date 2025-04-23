def cal_k_vinet(p, k):
    """
    calculate bulk modulus in GPa

    :param p: pressure in GPa
    :param k: [v0, k0, k0p]
    :return: bulk pressure at pressure pressure in GPa
    """
    return vinet(p, k[0], k[1], k[2])


