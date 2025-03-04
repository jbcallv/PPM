def keepOriginalText(s,startLoc,t):
    """DEPRECATED - based new helper method C{L{originalTextFor}}.
       a parse action to preserve original parsed text,
       overriding any other parse actions."""
    s.originalText[startLoc:s.loc] = t


