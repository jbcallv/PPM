def match(self, name):
		'''Compare an name same to the alias name.'''
		if (self.ns + self.name).startswith(name):
			return True

		for alias in self.aliases:
			if (self.ns + alias).startswith(name):
				return True

		return False

	def __str__(self):
		'''Return a string representation of the alias.'''
		return '%s = %s' % (self.alias, self.ns + self.name)

	def __repr__(self):
		'''Return a string representation of the alias.'''
		return self.__str__()

	def __eq__(self, other):
		'''Return true if the two aliases have the same namespace and name.'''
		return self.ns == other.ns and self.name == other.name

	def __ne__(self, other):
		'''Return true if the two aliases do not have the same namespace and name.'''
		return not self.__eq__(other)

