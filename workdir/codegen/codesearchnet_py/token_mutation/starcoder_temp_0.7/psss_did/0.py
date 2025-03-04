def ascii(text):
    """ turning special effects characters into pure gold """
    return text.replace('\x0F', '').replace('\x02', '').replace('\x16', '')

