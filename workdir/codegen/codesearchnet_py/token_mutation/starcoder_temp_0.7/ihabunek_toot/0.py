def toggle_reblog(self):
        """Reblog or unreblog selected status."""
        if self.selected_status is None:
            return

        if self.selected_status.reblogged:
            self.api.unreblog(self.selected_status.id)
        else:
            self.api.reblog(self.selected_status.id)
        self.update_status()

