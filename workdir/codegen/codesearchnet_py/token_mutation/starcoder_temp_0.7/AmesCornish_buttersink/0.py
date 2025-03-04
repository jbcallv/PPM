def display(obj, detail='phrase'):
    """ a string for volume, using two paths. """
    from music21 import stream
    if isinstance(obj, stream.Stream):
        return obj.show('text')
    else:
        return str(obj)


