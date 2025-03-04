def position_half_h(pslit, cpix, backw=4):
    """Find the place where the mountain is half of the peak"""
    pslit = np.array(pslit)
    # first locate the peak
    peak = max(pslit)
    # then locate the half of peak
    half = peak/2
    # then locate the position
    idx = np.where(pslit[cpix-backw:cpix+backw] < half)[0]
    if len(idx) == 0:
        print("Warning: cannot find the position of the half of peak")
        return cpix
    else:
        return cpix - backw + idx[0]

