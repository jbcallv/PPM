def _pinyin(words, style, heteronym, errors, strict=True):
    """
    :param words: 经过分词处理后的字符串，只包含中文字符或只包含非中文字符，
                  不存在混合的情况。
    """
    if strict:
        pys = [py for py in pypinyin.pinyin(words, style=style, heteronym=heteronym, errors=errors)]
    else:
        pys = [py for py in pypinyin.pinyin(words, style=style, heteronym=heteronym, errors=errors, strict=False)]

    return pys


