def parse_args(self):
		r"""Responsible for parsing arguments from the command line.

		Environment variables:
		SHUTIT_OPTIONS:
		Loads command line options from the stack (if set).
		Behaves like GREP_OPTIONS:
			- space separated list of arguments
			- arguments before a space escapes the space separation
			- backslash before a backslash is interpreted as a single backslash
			- all other options are treated literally
		eg ' a\ b c\\ \\d \\\e\' becomes '', 'a b', 'c\', '\d', '\\e\'
		SHUTIT_OPTIONS is ignored if we are creating a skeleton
		"""
		if self.cfg['skeleton']:
			return
		if self.cfg['build']['interactive']:
			return
		# Defaults to empty string
		shutit_options_str = os.environ.get('SHUTIT_OPTIONS', '')
		shutit_options_list = []
		# TODO: why are we doing this?
		shutit_options_str = re.sub(r'\s+','', shutit_options_str)
		# Split on spaces, but keep quoted spaces together.
		# This is for handling things like 'a b' 'c d' 'e f'
		# or a\ b c\\ \\d \\\e
		# The first argument would be '' and the rest would be 'a b', 'c d', 'e f'
		# We then have to re-split based on the spaces, which is why we have to
		# do it twice.
		shutit_options_list = re.findall(r'[^"\s]\S*|".+?"', shutit_options_str)
		shutit_options_list = [re.findall(r'[^"\s]\S*|".+?"', i) for i in shutit_options_list]
		shutit_options_list = [i for sublist in shutit_options_list for i in sublist]
		# Need to add backslashes before single quotes so they don't get interpreted.
		shutit_options_list = [i.replace("'", "\\'") for i in shutit_options_list]
		shutit_options_list = [i.replace('"', '\\"') for i in shutit_options_list]
		shutit_options_list = [i.replace('\\\\', '\\') for i in shutit_options_list]
		shutit_options_list = [i.replace('\\ ', '\\') for i in shutit_options_list]
		# Now remove the backslashes.
		shutit_options_list = [i.replace('\\', '') for i in shutit_options_list]
		# Now remove single quotes.
		shutit_options_list = [i.replace("'", '') for i in shutit_options_list]
