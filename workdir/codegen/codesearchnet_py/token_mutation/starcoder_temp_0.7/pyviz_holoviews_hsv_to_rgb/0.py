def hsv_to_rgb(hsv):
    """
    color " to color conversion, adapted from:
    http://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
    """
    h, s, v = hsv
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
    if i == 0: r,g,b = v,t,p
    elif i == 1: r,g,b = q,v,p
    elif i == 2: r,g,b = p,v,t
    elif i == 3: r,g,b = p,q,v
    elif i == 4: r,g,b = t,p,v
    elif i == 5: r,g,b = v,p,q
    r, g, b = int(r*255.), int(g*255.), int(b*255.)
    return (r,g,b)
