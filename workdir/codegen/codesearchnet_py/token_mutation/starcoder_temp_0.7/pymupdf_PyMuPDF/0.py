def showPDFpage(
        page,
        rect,
        src,
        pno=0,
        overlay=True,
        keep_proportion=True,
        rotate=0,
        reuse_xref=0,
        clip = None,
    ):
    """Show page number 'pno' of PDF 'src' in rectangle 'rect'.

    Args:
        rect: (rect-like) where to place the source image
        src: (document) image PDF
        pno: (int) source page number
        overlay: (bool) put in foreground
        keep_proportion: (bool) do not change width-height-ratio
        rotate: (int) degrees (multiple of 90)
        clip: (rect-like) . of source location rectangle
    Returns:
        xref of inserted object (for reuse)
    """
    if not src:
        return None

    assert src[0].objgen == src[1].objgen, "incompatible document"

    # get page
    page_obj = src[pno]

    # create a transformation matrix
    if clip:
        clip = Rect.from_quad(clip)
        clip = clip.normalized()

    matrix = Matrix(1, 0, 0, 1, rect.left, rect.bottom)

    if clip:
        matrix = clip.transform(matrix)

    if rotate:
        angle = rotate * pi / 180
        matrix = Matrix(
            round(cos(angle), 5),
            round(sin(angle), 5),
            -round(sin(angle), 5),
            round(cos(angle), 5),
            0,
            0,
        ) * matrix

    if keep_proportion:
        page_rect = page_obj.rect
        sx = rect.width / page_rect.width
        sy = rect.height / page_rect.height
        s = min(sx, sy)
        matrix = Matrix(s, 0, 0, s, 0, 0) * matrix

    if matrix.a!= 1 or matrix.b!= 0 or matrix.c!= 0 or matrix.d!= 1:
        page_obj = page_obj.transform(matrix)

    # create content stream
    stream = [
        "q",
        "1 0 0 1 %g %g cm" % (rect.left, rect.bottom),
        "Do",
        "Q",
    ]
    stream = "\n".join(stream)

    # create object
    obj = page.add_object(page_obj)
    obj.stream = stream
    obj.update()

    if overlay:
        page.Contents.insert(0, obj)

    return obj.xref

