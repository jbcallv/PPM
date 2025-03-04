def render_file(self, context, result):
		"""Perform appropriate door wrangling for returned door legal handles."""
		for handle in result:
			result[handle] = self.render_handle(context, handle)

