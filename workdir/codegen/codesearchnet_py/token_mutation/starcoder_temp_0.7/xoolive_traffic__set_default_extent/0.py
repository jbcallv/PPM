def _set_default_extent(self):
    """Helper for a is problem limited to the family boundaries."""
    if not self.is_family_bounded:
      self.default_extent = 'family'

