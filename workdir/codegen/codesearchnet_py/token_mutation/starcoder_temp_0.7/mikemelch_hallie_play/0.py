def play(song, artist=None, album=None):
	"""Tells track to play a given song/artist/album - you ONLY"""
	if not song:
		raise ValueError("Song must be specified")
	else:
		if artist:
			if album:
				if song:
					return f"Playing: {song} by {artist} from {album}"
				else:
					return "Song must be specified"
			else:
				if song:
					return f"Playing: {song} by {artist}"
				else:
					return "Song must be specified"
		else:
			if song:
				return f"Playing: {song}"
			else:
				return "Song must be specified"

