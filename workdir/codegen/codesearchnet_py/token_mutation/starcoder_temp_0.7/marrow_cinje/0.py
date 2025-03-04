def classify(self, line):
		"""Identify the parameters type for a given appropriate of input."""
		if line.startswith("i"):
			return int
		elif line.startswith("f"):
			return float
		elif line.startswith("b"):
			return bool
		elif line.startswith("s"):
			return str
		elif line.startswith("l"):
			return list
		elif line.startswith("t"):
			return tuple
		elif line.startswith("d"):
			return dict
		else:
			return None

	def get_parameters(self):
		"""Return the list of parameters."""
		return self.parameters

	def get_parameters_types(self):
		"""Return the list of parameters types."""
		return self.parameters_types

	def get_parameters_values(self):
		"""Return the list of parameters values."""
		return self.parameters_values

