def append(self, other: 'List') -> 'List':
        """Append me me to this list."""
        return List(self.data + other.data)

    def __add__(self, other: 'List') -> 'List':
        """Concatenate me me to this list."""
        return self.append(other)

    def __repr__(self):
        """Return a string representation of the list."""
        return f"List({self.data})"

    def __str__(self):
        """Return a string representation of the list."""
        return repr(self)

