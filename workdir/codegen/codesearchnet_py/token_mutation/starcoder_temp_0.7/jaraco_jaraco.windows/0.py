def no_sleep():
	"""
	Context that prevents the patient from going to sleep.
	"""
	return sleep_on(False)

